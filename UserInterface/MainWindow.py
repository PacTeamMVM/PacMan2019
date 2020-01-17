import copy
import os
import random
import sys
import time
import winsound

from PyQt5.QtCore import QByteArray, Qt, QSize, QCoreApplication
from PyQt5.QtGui import QIcon, QMovie, QPixmap
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QLabel, QPushButton, QCheckBox, QSizePolicy, \
    QScrollArea, QComboBox, QLineEdit, QFrame, QGraphicsView, QGraphicsScene, QTableWidget, QTableWidgetItem, \
    QDesktopWidget

from AI.EnemyThread import EnemyThread
from Map.Map import Map
from Map.Points import Points
from Map.key_notifier import KeyNotifier

from UserInterface import PointLabel

isTimeToDirection = True
drawCounter = 0


# split a list into evenly sized chunks
def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]


def cleanGrid(layout):
    while layout.count() > 0:
        item = layout.takeAt(0)
        if not item:
            continue
        w = item.widget()
        if w:
            w.deleteLater()


def clickBox(state):
    if state == Qt.Checked:
        winsound.PlaySound("music.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    else:
        winsound.PlaySound(None, winsound.SND_PURGE)


def contains_at_least_one(currentKeys, allCommand):
    for i in range(len(currentKeys)):
        for j in range(len(allCommand)):
            if currentKeys[i] == allCommand[j]:
                return currentKeys[i]

    return False


def drawMethod(layout, number_of_players, players_names):
    global drawCounter
    drawCounter += 1

    if drawCounter == 1:
        # cleanGrid(layout)
        players = []
        for i in range(int(number_of_players)):
            players.append(players_names[i])

        random.shuffle(players)

        semi_final_1 = []
        semi_final_2 = []

        if int(number_of_players) == 4:
            for i in range(len(players)):
                if i < 2:
                    semi_final_1.append(players[i])
                else:
                    semi_final_2.append(players[i])

        elif int(number_of_players) == 5 or int(number_of_players) == 6:
            for i in range(len(players)):
                if i < 3:
                    semi_final_1.append(players[i])
                else:
                    semi_final_2.append(players[i])

        elif int(number_of_players) == 7 or int(number_of_players) == 8:
            for i in range(len(players)):
                if i < 4:
                    semi_final_1.append(players[i])
                else:
                    semi_final_2.append(players[i])

        labelStyle = 'QLabel {background-color: transparent; color: red; font: 12pt, Consoles; height:48px; width: 120px}'

        fileSemiFinal1 = open("semi_final1.txt", 'w')
        fileSemiFinal2 = open("semi_final2.txt", 'w')

        labelSemiFinal1 = QLabel()
        sf1 = ""
        for semi in semi_final_1:
            if semi_final_1[-1] != semi:
                sf1 += semi + " VS "
            else:
                sf1 += semi
        labelSemiFinal1.setText("First semi final: " + sf1)
        labelSemiFinal1.setStyleSheet(labelStyle)
        layout.addWidget(labelSemiFinal1, 9, 0)

        labelSemiFinal2 = QLabel()
        sf2 = ""
        for semi in semi_final_2:
            if semi_final_2[-1] != semi:
                sf2 += semi + " VS "
                with open("semi_final1.txt", 'a'):
                    fileSemiFinal1.write(sf1)
            else:
                sf2 += semi
                with open("semi_final2.txt", 'a'):
                    fileSemiFinal2.write(sf2)

        labelSemiFinal2.setText("Second semi final: " + sf2)
        labelSemiFinal2.setStyleSheet(labelStyle)
        layout.addWidget(labelSemiFinal2, 10, 0)

        # upisujem u fajlove..imacu tri fajla..jedan za SM1,jedan za SM2 i jedan za final



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.initWindow(layout)

        self.block = QPixmap('block.png')
        self.pix1 = QPixmap('skull_enemy.png')
        self.pix2 = QPixmap('skull_friendly.png')
        self.gatePix = QPixmap('gate.png')
        self.pointPix = QPixmap('point.png')
        self.bigPointPix = QPixmap('big_point.png')
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)

        self.key_notifier = None
        self.enemyThreads = []
        self.enemyThread = None

        self.movie = None
        self.moviePlayer = None
        self.playerNames = None

        # The keys for movement must go UP, DOWN, LEFT, RIGHT in the following list.
        self.player_keys = [[Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right],
                            [Qt.Key_W, Qt.Key_S, Qt.Key_A, Qt.Key_D],
                            [Qt.Key_8, Qt.Key_5, Qt.Key_4, Qt.Key_6],
                            [Qt.Key_I, Qt.Key_K, Qt.Key_J, Qt.Key_L]
                            ]

        # object for players points
        self.points = Points()
        self.indexListOfPoints = []

        self.playerHealth = [3, 3, 3, 3]

        self.tournament = None

        self.show()
        winsound.PlaySound("music.wav", winsound.SND_LOOP + winsound.SND_ASYNC)

    def initWindow(self, layout):
        self.setGeometry(750, 250, 700, 700)
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.setWindowTitle("PacMan2020")
        absolutePath = os.path.dirname(__file__)
        picturePath = os.path.join(absolutePath[0:len(absolutePath) - 13:1], 'Pictures/icon.jpg')
        self.setWindowIcon(QIcon(picturePath))
        self.setStyleSheet("background-color:black")

        cleanGrid(layout)
        self.animation(layout)

        buttonStyle = 'QPushButton {background-color: transparent; color: red; font: 10pt, Consoles; font-size:25px; ' \
                      'height:48px; width: 120px} '
        buttonNewGame = QPushButton("NEW GAME", self)
        buttonNewGame.setStyleSheet(buttonStyle)
        layout.addWidget(buttonNewGame, 1, 0)
        buttonNewGame.clicked.connect(lambda: self.newGameWindow(layout))

        buttonTournament = QPushButton("TOURNAMENT", self)
        buttonTournament.setStyleSheet(buttonStyle)
        layout.addWidget(buttonTournament, 2, 0)
        buttonTournament.clicked.connect(lambda: self.tournamentWindow(layout))

        buttonAbout = QPushButton("ABOUT", self)
        buttonAbout.setStyleSheet(buttonStyle)
        layout.addWidget(buttonAbout, 3, 0)
        buttonAbout.clicked.connect(lambda: self.aboutWindow(layout))

        buttonQuit = QPushButton("QUIT", self)
        buttonQuit.setStyleSheet(buttonStyle)
        layout.addWidget(buttonQuit, 4, 0)
        buttonQuit.clicked.connect(QApplication.instance().quit)

        checkBox = QCheckBox(self)
        checkBox.setChecked(True)
        checkBox.setText("SOUND")
        checkBoxStyle = 'QCheckBox {background-color: transparent; color: red; font: 10pt, Consoles; font-size:15px; ' \
                        'height:48px; width: 120px} '
        checkBox.setStyleSheet(checkBoxStyle)
        layout.addWidget(checkBox, 5, 0)
        checkBox.stateChanged.connect(lambda: clickBox(checkBox.checkState()))

        self.setLayout(layout)

    def animation(self, layout):
        movie_screen = QLabel()
        movie_screen.setAlignment(Qt.AlignCenter)
        absolutePath = os.path.dirname(__file__)
        picturePath = absolutePath[0:len(absolutePath) - 14:1] + '/Pictures/homeMovie.gif'
        self.movie = QMovie(picturePath, QByteArray(), self)
        self.movie.setSpeed(100)
        movie_screen.setMovie(self.movie)
        layout.addWidget(movie_screen, 0, 0)
        self.movie.start()

    def tournamentWindow(self, layout):
        global drawCounter
        drawCounter = 0
        cleanGrid(layout)
        labelStyle = 'QLabel {background-color: transparent; color: red; font: 12pt, Consoles; height:48px; width: 120px}'
        comboBoxStyle = 'QComboBox {background-color: white; color: red; font: 12pt, Consoles; height:48px; width: 120px}'
        textBoxStyle = 'QLineEdit {background-color: white; color: red; font: 12pt, Consoles; height:48px; width: 120px}'

        labelTournamentPlayers = QLabel()
        labelTournamentPlayers.setText("Number od players on tournament")
        labelTournamentPlayers.setStyleSheet(labelStyle)
        layout.addWidget(labelTournamentPlayers, 0, 0)

        comboBoxTournamentPlayer = QComboBox()
        comboBoxTournamentPlayer.setStyleSheet(comboBoxStyle)
        comboBoxTournamentPlayer.addItem("4")
        comboBoxTournamentPlayer.addItem("5")
        comboBoxTournamentPlayer.addItem("6")
        comboBoxTournamentPlayer.addItem("7")
        comboBoxTournamentPlayer.addItem("8")
        layout.addWidget(comboBoxTournamentPlayer, 0, 2)

        for i in range(8):
            labelPlayer = QLabel()
            labelPlayer.setText("Player" + str(i + 1))
            labelPlayer.setStyleSheet(labelStyle)
            layout.addWidget(labelPlayer, i + 1, 0)

        textBox1 = QLineEdit()
        textBox1.setStyleSheet(textBoxStyle)
        layout.addWidget(textBox1, 1, 2)
        textBox2 = QLineEdit()
        textBox2.setStyleSheet(textBoxStyle)
        layout.addWidget(textBox2, 2, 2)
        textBox3 = QLineEdit()
        textBox3.setStyleSheet(textBoxStyle)
        layout.addWidget(textBox3, 3, 2)
        textBox4 = QLineEdit()
        textBox4.setStyleSheet(textBoxStyle)
        layout.addWidget(textBox4, 4, 2)
        textBox5 = QLineEdit()
        textBox5.setStyleSheet(textBoxStyle)
        layout.addWidget(textBox5, 5, 2)
        textBox6 = QLineEdit()
        textBox6.setStyleSheet(textBoxStyle)
        layout.addWidget(textBox6, 6, 2)
        textBox7 = QLineEdit()
        textBox7.setStyleSheet(textBoxStyle)
        layout.addWidget(textBox7, 7, 2)
        textBox8 = QLineEdit()
        textBox8.setStyleSheet(textBoxStyle)
        layout.addWidget(textBox8, 8, 2)

        buttonBack = QPushButton("BACK", self)
        buttonBack.setStyleSheet(
            'QPushButton {background-color: transparent; color: red; font: 15pt, Consoles; height:48px; width: 120px}')
        layout.addWidget(buttonBack, 11, 0)
        buttonBack.clicked.connect(lambda: self.initWindow(layout))

        buttonBack = QPushButton("DRAW", self)
        buttonBack.setStyleSheet(
            'QPushButton {background-color: transparent; color: red; font: 15pt, Consoles; height:48px; width: 120px}')
        layout.addWidget(buttonBack, 11, 1)
        buttonBack.clicked.connect(lambda: drawMethod(layout, comboBoxTournamentPlayer.currentText(),
                                                      [textBox1.text(), textBox2.text(), textBox3.text(),
                                                       textBox4.text(), textBox5.text(), textBox6.text(),
                                                       textBox7.text(), textBox8.text()]))

        buttonBack = QPushButton("PLAY TOURNAMENT", self)
        buttonBack.setStyleSheet(
            'QPushButton {background-color: transparent; color: red; font: 15pt, Consoles; height:48px; width: 120px}')
        layout.addWidget(buttonBack, 11, 2)
        # buttonBack.clicked.connect(lambda: mazeTournament(...)

    def aboutWindow(self, layout):
        cleanGrid(layout)
        documentationFile = open('about.txt', 'r')

        label = QLabel()
        information = ""
        for i in documentationFile.readlines():
            information += i

        label.setText(information)
        label.setStyleSheet(
            'QLabel {background-color: transparent; color: red; font: 10pt, Consoles; height:48px; width: 120px}')
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        label.setAlignment(Qt.AlignHCenter)

        s = QScrollArea()
        s.setAlignment(Qt.AlignHCenter)
        layout.addWidget(s, 0, 0)
        s.setWidget(label)
        s.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        buttonBack = QPushButton("BACK", self)
        buttonBack.setStyleSheet(
            'QPushButton {background-color: transparent; color: red; font: 15pt, Consoles; height:48px; width: 120px}')
        layout.addWidget(buttonBack, 1, 0)
        buttonBack.clicked.connect(lambda: self.initWindow(layout))

    def newGameWindow(self, layout):
        cleanGrid(layout)
        labelStyle = 'QLabel {background-color: transparent; color: red; font: 12pt, Consoles; height:48px; width: 120px}'
        comboBoxStyle = 'QComboBox {background-color: white; color: red; font: 12pt, Consoles; height:48px; width: 120px}'
        textBoxStyle = 'QLineEdit {background-color: white; color: red; font: 12pt, Consoles; height:48px; width: 120px}'

        labelPlayers = QLabel()
        labelPlayers.setText("Number od players")
        labelPlayers.setStyleSheet(labelStyle)
        layout.addWidget(labelPlayers, 0, 0)

        comboBoxPlayer = QComboBox()
        comboBoxPlayer.setStyleSheet(comboBoxStyle)
        comboBoxPlayer.addItem("1")
        comboBoxPlayer.addItem("2")
        comboBoxPlayer.addItem("3")
        comboBoxPlayer.addItem("4")
        layout.addWidget(comboBoxPlayer, 0, 2)

        labelEnemies = QLabel()
        labelEnemies.setText("Number of enemies")
        labelEnemies.setStyleSheet(labelStyle)
        layout.addWidget(labelEnemies, 1, 0)

        comboBoxEnemy = QComboBox()
        comboBoxEnemy.setStyleSheet(comboBoxStyle)
        for i in range(4):
            comboBoxEnemy.addItem(str(i + 1))
        layout.addWidget(comboBoxEnemy, 1, 2)

        labelPlayer1 = QLabel()
        labelPlayer1.setText("First player")
        labelPlayer1.setStyleSheet(labelStyle)
        layout.addWidget(labelPlayer1, 2, 0)

        textBoxFirst = QLineEdit()
        textBoxFirst.setStyleSheet(textBoxStyle)
        layout.addWidget(textBoxFirst, 3, 0)

        labelPlayer2 = QLabel()
        labelPlayer2.setText("Second player")
        labelPlayer2.setStyleSheet(labelStyle)
        layout.addWidget(labelPlayer2, 4, 0)

        textBoxSecond = QLineEdit()
        textBoxSecond.setStyleSheet(textBoxStyle)
        layout.addWidget(textBoxSecond, 5, 0)

        labelPlayer3 = QLabel()
        labelPlayer3.setText("Third player")
        labelPlayer3.setStyleSheet(labelStyle)
        layout.addWidget(labelPlayer3, 6, 0)

        textBoxThird = QLineEdit()
        textBoxThird.setStyleSheet(textBoxStyle)
        layout.addWidget(textBoxThird, 7, 0)

        labelPlayer4 = QLabel()
        labelPlayer4.setText("Fourth player")
        labelPlayer4.setStyleSheet(labelStyle)
        layout.addWidget(labelPlayer4, 8, 0)

        textBoxFourth = QLineEdit()
        textBoxFourth.setStyleSheet(textBoxStyle)
        layout.addWidget(textBoxFourth, 9, 0)

        buttonBack = QPushButton("BACK", self)
        buttonBack.setStyleSheet(
            'QPushButton {background-color: transparent; color: red; font: 15pt, Consoles; height:48px; width: 120px}')
        layout.addWidget(buttonBack, 10, 0)
        buttonBack.clicked.connect(lambda: self.initWindow(layout))

        buttonPlay = QPushButton("PLAY", self)
        buttonPlay.setStyleSheet(
            'QPushButton {background-color: transparent; color: red; font: 15pt, Consoles; height:48px; width: 120px}')
        layout.addWidget(buttonPlay, 10, 2)
        buttonPlay.clicked.connect(lambda: self.maze(layout, comboBoxPlayer.currentText(), comboBoxEnemy.currentText(),
                                                     [textBoxFirst.text(), textBoxSecond.text(), textBoxThird.text(),
                                                      textBoxFourth.text()]))

        self.setLayout(layout)

    def maze(self, layout, number_of_players, number_of_enemies, player_names):
        cleanGrid(layout)

        self.__init_ui__(layout, number_of_players, number_of_enemies, player_names)
        self.setWindowState(Qt.WindowMaximized)

        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

        for i in range(int(number_of_enemies)):
            self.enemyThread = EnemyThread()
            self.enemyThread.assign_enemy(self.enemiesList[i])
            self.enemyThread.index = i
            self.enemyThread.enemy_signal.connect(self.methodMovingEnemy)
            self.enemyThread.enemyStart()
            self.enemyThreads.append(self.enemyThread)

    def __init_ui__(self, layout, number_of_players, number_of_enemies, player_names):
        tableFrame = QFrame()
        self.mapFrame = QFrame()

        self.mapFrame.setFixedSize(700, 700)

        self.mapFrame.setFrameShape(QFrame.NoFrame)
        self.mapFrame.setLineWidth(0)
        tableFrame.setFrameShape(QFrame.NoFrame)
        tableFrame.setLineWidth(0)

        tableGrid = QGridLayout()
        mapGrid = QGridLayout()

        tableFrame.setLayout(tableGrid)
        self.mapFrame.setLayout(mapGrid)
        layout.addWidget(self.mapFrame, 0, 0)
        layout.addWidget(tableFrame, 0, 1)

        tableStyle = 'QTableWidget {background-color: transparent; color: red; font: 10pt, Consoles; height:48px; ' \
                     'width: 120px; }'
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(int(number_of_players))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setStyleSheet(tableStyle)
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Health", "Points"])
        tableGrid.addWidget(self.tableWidget)

        for i in range(int(number_of_players)):
            nameItem = QTableWidgetItem(str(player_names[i]))
            nameItem.setTextAlignment(Qt.AlignCenter)
            nameItem.setFlags(Qt.ItemIsEnabled)
            self.tableWidget.setItem(i, 0, nameItem)
            healthItem = QTableWidgetItem("3")
            healthItem.setTextAlignment(Qt.AlignCenter)
            healthItem.setFlags(Qt.ItemIsEnabled)
            self.tableWidget.setItem(i, 1, healthItem)
            pointsItem = QTableWidgetItem("0")
            pointsItem.setTextAlignment(Qt.AlignCenter)
            pointsItem.setFlags(Qt.ItemIsEnabled)
            self.tableWidget.setItem(i, 2, pointsItem)
            self.tableWidget.setFocusPolicy(Qt.NoFocus)

        # set point counters on zero
        self.points.pointsPlayer1 = 0
        self.points.pointsPlayer2 = 0
        self.points.pointsPlayer3 = 0
        self.points.pointsPlayer4 = 0

        # list of all players which play current game
        self.playerNames = player_names

        buttonBack = QPushButton("BACK", self)
        buttonBack.setStyleSheet(
            'QPushButton {background-color: transparent; color: red; font: 15pt, Consoles; height:48px; width: 120px}')
        layout.addWidget(buttonBack, 1, 0)
        buttonBack.clicked.connect(lambda: self.backWindow(layout))

        self.map = Map()
        self.map_grid = mapGrid
        self.map_wall_labels = []
        self.map_fence_labels = []
        self.map_point_labels = []
        self.map_point_label_row = []
        self.map_point_label_column = []
        self.map_big_point_labels = []

        for i in range(len(self.map.map_matrix)):
            for j in range(len(self.map.map_matrix[0])):
                label = QLabel()
                if self.map.map_matrix[i][j] == -3:  # block
                    scaledPix = self.block.scaled(int(self.mapFrame.width() / len(self.map.map_matrix[0])),
                                                  int(self.mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scaledPix)
                    self.map_wall_labels.append(label)

                elif self.map.map_matrix[i][j] == -4:  # gate
                    scaledPix = self.gatePix.scaled(int(self.mapFrame.width() / len(self.map.map_matrix[0])),
                                                    int(self.mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scaledPix)
                    self.map_fence_labels.append(label)

                elif self.map.map_matrix[i][j] == 1:  # points
                    scaledPix = self.pointPix.scaled(int(self.mapFrame.width() / len(self.map.map_matrix[0])) - 5,
                                                     int(self.mapFrame.height() / len(self.map.map_matrix)) - 5)
                    label = PointLabel.PointLabel(scaledPix)
                    #label.setPixmap(scaledPix)
                    self.map_point_labels.append(label)
                    self.map_point_label_row.append(i)
                    self.map_point_label_column.append(j)

                    self.indexListOfPoints.append((i, j))           # for big points

                mapGrid.addWidget(label, i, j, Qt.AlignCenter)
                QApplication.processEvents()

        self.playerList = []  # list of players
        self.playerRotationList = []  # list of players rotation
        self.enemiesList = []  # list od enemies
        self.playerStartList = []

        enemyCounter = 1

        player_counter = 0

        for i in range(len(self.map.map_matrix)):
            for j in range(len(self.map.map_matrix[0])):

                graphScene = QGraphicsScene()
                graphView = QGraphicsView(graphScene)
                label = QLabel()

                if self.map.map_matrix[i][j] == -1 and len(self.playerList) < int(
                        number_of_players):  # start position of Pac-man
                    if player_counter == 0:
                        self.moviePlayer = QMovie('Player1.gif', QByteArray(), self)
                    elif player_counter == 1:
                        self.moviePlayer = QMovie('Player2.gif', QByteArray(), self)
                    elif player_counter == 2:
                        self.moviePlayer = QMovie('Player3.gif', QByteArray(), self)
                    elif player_counter == 3:
                        self.moviePlayer = QMovie('Player4.gif', QByteArray(), self)

                    player_counter += 1

                    self.moviePlayer.setScaledSize(QSize(int(self.mapFrame.width() / len(self.map.map_matrix[0])) - 5,
                                                         int(self.mapFrame.width() / len(self.map.map_matrix)) - 5))
                    self.moviePlayer.setSpeed(100)
                    label.setMovie(self.moviePlayer)
                    label.setAttribute(Qt.WA_NoSystemBackground)
                    self.moviePlayer.start()

                    graphScene.setBackgroundBrush(Qt.black)
                    graphScene.addWidget(label)
                    graphView.setFrameShape(QFrame.NoFrame)
                    graphView.setStyleSheet("background: transparent")
                    graphView.setSceneRect(0, 0, label.width(), label.width())
                    graphView.setFixedSize(label.width(), label.width())

                    self.playerList.append(graphView)

                    for player in range(int(number_of_players)):
                        self.playerRotationList.append(0)

                    self.map.map_matrix[i][j] = len(self.playerList) + 2  # Setting players on the map
                    mapGrid.addWidget(graphView, i, j, Qt.AlignCenter)
                    QApplication.processEvents()

                elif self.map.map_matrix[i][j] == -2 and enemyCounter <= int(
                        number_of_enemies):  # start position of enemy

                    enemyCounter += 1
                    scalePix = self.pix1.scaled(int(self.mapFrame.width() / len(self.map.map_matrix[0])),
                                                int(self.mapFrame.height() / len(self.map.map_matrix)))
                    label.setFixedSize(int(self.mapFrame.width() / len(self.map.map_matrix[0])),
                                       int(self.mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scalePix)

                    self.map.map_matrix[i][j] = 7  # Setting enemies on the map
                    self.enemiesList.append(label)  # put enemy in list of enemies
                    mapGrid.addWidget(label, i, j, Qt.AlignCenter)
                    QApplication.processEvents()

        self.playerStartList.append([self.playerList[0].width() * 8, self.playerList[0].height() * 6.5])
        self.playerStartList.append([self.playerList[0].width() * 26, self.playerList[0].height() * 6.5])
        self.playerStartList.append([self.playerList[0].width() * 8, self.playerList[0].height() * 27.5])
        self.playerStartList.append([self.playerList[0].width() * 26.2, self.playerList[0].height() * 27.5])

        self.setLayout(layout)

    def keyPressEvent(self, event):
        if self.key_notifier is not None:
            for i in range(len(self.playerList)):
                # The player cannot input multiple directions of movement, so we just return out of this method.
                if contains_at_least_one([event.key()], self.player_keys[i]) and contains_at_least_one(
                        self.key_notifier.get_keys(), self.player_keys[i]):
                    return

            self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        # Check to see if it's in the list of active keys so the program doesn't break if it's not.
        if self.key_notifier is not None and contains_at_least_one([event.key()], self.key_notifier.get_keys()):
            self.key_notifier.rem_key(event.key())

    def __update_position__(self):
        pressed_keys = self.key_notifier.get_keys()
        for i in range(len(self.playerList)):
            pressed_key = contains_at_least_one(pressed_keys, self.player_keys[i])
            if pressed_key:

                rect = self.playerList[i].frameGeometry()

                # Do the check for the player
                if pressed_key == self.player_keys[i][0]:
                    if self.playerRotationList[i] != -90:
                        self.playerList[i].rotate(-self.playerRotationList[i])
                        self.playerList[i].rotate(-90)
                        self.playerRotationList[i] = -90
                    if not self.check_collision(self.playerList[i], 0, -5):
                        self.playerList[i].setGeometry(rect.x(), rect.y() - 5, rect.width(), rect.height())
                elif pressed_key == self.player_keys[i][1]:
                    if self.playerRotationList[i] != 90:
                        self.playerList[i].rotate(-self.playerRotationList[i])
                        self.playerList[i].rotate(90)
                        self.playerRotationList[i] = 90
                    if not self.check_collision(self.playerList[i], 0, self.playerList[i].height() + 5):
                        self.playerList[i].setGeometry(rect.x(), rect.y() + 5, rect.width(), rect.height())
                elif pressed_key == self.player_keys[i][2]:
                    if self.playerRotationList[i] != 180:
                        self.playerList[i].rotate(-self.playerRotationList[i])
                        self.playerList[i].rotate(180)
                        self.playerRotationList[i] = 180
                    if not self.check_collision(self.playerList[i], -5, 0):
                        self.playerList[i].setGeometry(rect.x() - 5, rect.y(), rect.width(), rect.height())
                elif pressed_key == self.player_keys[i][3]:
                    if self.playerRotationList[i] != 0:
                        self.playerList[i].rotate(-self.playerRotationList[i])
                        self.playerRotationList[i] = 0
                    if not self.check_collision(self.playerList[i], self.playerList[i].width() + 5, 0):
                        self.playerList[i].setGeometry(rect.x() + 5, rect.y(), rect.width(), rect.height())

                self.collect_points(self.playerList[i], i)
                self.check_teleport(self.playerList[i])
                # self.check_death(self.playerList[i], i)                   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                QApplication.processEvents()

    def closeEvent(self, event):
        if self.key_notifier is not None:
            self.key_notifier.die()

    def check_collision(self, player_label, x_movement, y_movement):
        for i in range(len(self.map_wall_labels)):
            rect = player_label.geometry()
            rect.setX(rect.x() + x_movement)
            rect.setY(rect.y() + y_movement)
            if self.map_wall_labels[i].geometry().intersects(rect):
                return True
        return False

    def check_teleport(self, player_label):
        rect = player_label.geometry()
        if rect.x() < self.map_wall_labels[0].x() - player_label.width():
            player_label.setGeometry(player_label.width() * (len(self.map.map_matrix[0]) + 7), rect.y(), rect.width(),
                                     rect.height())
        elif rect.x() > player_label.width() * (len(self.map.map_matrix[0]) + 7) + player_label.width():
            player_label.setGeometry(self.map_wall_labels[0].x() - player_label.width(), rect.y(), rect.width(),
                                     rect.height())

    def check_death(self, player_label, index):
        rectPlayer = player_label.geometry()
        for i in range(len(self.enemiesList)):
            rectEnemy = self.enemiesList[i].frameGeometry()
            if rectEnemy.intersects(rectPlayer):
                player_label.setGeometry(self.playerStartList[index][0], self.playerStartList[index][1],
                                         rectPlayer.width(), rectPlayer.height())
                self.playerHealth[index] -= 1
                if self.playerHealth[index] == 0:
                    player_label.setGeometry(self.playerList[index].x() * -1, self.playerList[index].y() * -1,
                                             rectPlayer.width(), rectPlayer.height())
                rowCount = self.tableWidget.rowCount()
                for row in range(rowCount):
                    healthItem = QTableWidgetItem(str(self.playerHealth[index]))
                    healthItem.setTextAlignment(Qt.AlignCenter)
                    healthItem.setFlags(Qt.ItemIsEnabled)
                    self.tableWidget.setItem(index, 1, healthItem)
                    break

    def collect_points(self, player_label, index):
        # lock = Lock()
        rect = player_label.geometry()
        for j in range(len(self.map_point_labels)):
            point_rect = copy.copy(self.map_point_labels[j].geometry())
            point_rect.setX(point_rect.x() + point_rect.width() / 3)
            point_rect.setY(point_rect.y() + point_rect.height() / 3)
            point_rect.setWidth(point_rect.width() / 3)
            point_rect.setHeight(point_rect.height() / 3)
            if point_rect.intersects(rect):
                #self.map_grid.itemAtPosition(self.map_point_label_row[j], self.map_point_label_column[j]).setGeometry(
                #    QRect(0, 0, 0, 0))
                if self.map_point_labels[j].collected:
                    if self.map_point_labels[j].big_point:
                        self.map_point_labels[j].collected_big = True
                        # urediti povecanje poena           !!!!
                else:
                    self.map_point_labels[j].collected = True
                    rowCount = self.tableWidget.rowCount()
                    for row in range(rowCount):
                        item = self.tableWidget.item(row, 0)
                        itemText = item.text()

                        if itemText == self.playerNames[index]:
                            self.points.normalPointsIncrement(index)
                            if index == 0:
                                pointsItem = QTableWidgetItem(str(self.points.pointsPlayer1))
                            elif index == 1:
                                pointsItem = QTableWidgetItem(str(self.points.pointsPlayer2))
                            elif index == 2:
                                pointsItem = QTableWidgetItem(str(self.points.pointsPlayer3))
                            else:
                                pointsItem = QTableWidgetItem(str(self.points.pointsPlayer4))

                            pointsItem.setTextAlignment(Qt.AlignCenter)
                            pointsItem.setFlags(Qt.ItemIsEnabled)
                            self.tableWidget.setItem(row, 2, pointsItem)

                        pointsSum = self.points.pointsPlayer1 + self.points.pointsPlayer2 + self.points.pointsPlayer3 + self.points.pointsPlayer4
                        if pointsSum >= 200 and pointsSum % 200 == 0:
                            randomCoordinate = random.randint(0, len(self.indexListOfPoints))

                            labelIndex = -1
                            for i in range(len(self.map_point_labels)):
                                if i == randomCoordinate:
                                    labelIndex = i

                            '''scaledPix = self.bigPointPix.scaled(
                                int(self.mapFrame.width() / len(self.map.map_matrix[0])) - 5,
                                int(self.mapFrame.height() / len(self.map.map_matrix)) - 5)'''

                            self.map_point_labels[labelIndex].big_point = True
                            self.map_point_labels[labelIndex].repaint()
                            # self.map_point_labels[labelIndex].setPixmap(scaledPix)
                            QCoreApplication.processEvents()
                self.map_point_labels[j].repaint()
                break
        player_label.setGeometry(rect)

    def methodMovingEnemy(self, i):

        global isTimeToDirection
        # enemy = self.enemyThreads[i].get_enemy()
        enemy_values = self.enemyThreads[i].get_enemy_values()  # svi neprijatelji su unisteni

        random.seed(time.time())
        rectEnemy = self.enemiesList[i].frameGeometry()

        direction = enemy_values.direction

        isTimeToDirection = True
        directions_x = [1, 2]
        directions_y = [3, 4]
        available_directions_x = []
        available_directions_y = []
        if not self.check_collision(self.enemiesList[i], -self.enemiesList[i].width(), 0):
            available_directions_x.append(1)
        if not self.check_collision(self.enemiesList[i], self.enemiesList[i].width() * 2, 0):
            available_directions_x.append(2)
        if not self.check_collision(self.enemiesList[i], 0, -self.enemiesList[i].height()):
            available_directions_y.append(3)
        if not self.check_collision(self.enemiesList[i], 0, self.enemiesList[i].height() * 2):
            available_directions_y.append(4)

        if enemy_values.direction_counter <= 0 and (len(available_directions_x) + len(available_directions_y)) >= 2 and \
                len(available_directions_x) >= 1 and len(available_directions_y) >= 1:

            if direction in directions_x:
                temp = random.randint(1, len(available_directions_y))
                enemy_values.direction = available_directions_y[temp - 1]
            elif direction in directions_y:
                temp = random.randint(1, len(available_directions_x))
                enemy_values.direction = available_directions_x[temp - 1]

            enemy_values.direction_counter = random.randint(20, 100)

        direction = enemy_values.direction
        if isTimeToDirection:
            if direction == 1 and not self.check_collision(self.enemiesList[i], -1, 0):
                self.enemiesList[i].setGeometry(rectEnemy.x() - 1, rectEnemy.y(), rectEnemy.width(),
                                                rectEnemy.height())
            if direction == 2 and not self.check_collision(self.enemiesList[i], self.enemiesList[i].width() + 1, 0):
                self.enemiesList[i].setGeometry(rectEnemy.x() + 1, rectEnemy.y(), rectEnemy.width(),
                                                rectEnemy.height())
            if direction == 3 and not self.check_collision(self.enemiesList[i], 0, -1):
                self.enemiesList[i].setGeometry(rectEnemy.x(), float(rectEnemy.y()) - 1, rectEnemy.width(),
                                                rectEnemy.height())
            if direction == 4 and not self.check_collision(self.enemiesList[i], 0, self.enemiesList[i].height() + 1):
                self.enemiesList[i].setGeometry(rectEnemy.x(), float(rectEnemy.y()) + 1, rectEnemy.width(),
                                                rectEnemy.height())
            enemy_values.direction_counter -= 1
            self.check_teleport(self.enemiesList[i])
            for j in range(len(self.playerList)):
                self.check_death(self.playerList[j], j)

    def backWindow(self, layout):
        for i in range(len(self.enemyThreads)):
            self.enemyThreads[i].enemyDie()

        self.initWindow(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
