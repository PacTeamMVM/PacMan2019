import copy
import os
import sys
import winsound

from PyQt5.QtCore import QByteArray, Qt, QSize, QRect
from PyQt5.QtGui import QIcon, QMovie, QPixmap
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QLabel, QPushButton, QCheckBox, QSizePolicy, \
    QScrollArea, QComboBox, QLineEdit, QFrame, QGraphicsView, QGraphicsScene, QTableWidget, QTableWidgetItem, \
    QDesktopWidget

from AI.EnemyThread import EnemyThread
from Map.Map import Map
from Map.Points import Points
from Map.key_notifier import KeyNotifier


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
        self.enemyThread = None

        self.movie = None
        self.moviePlayer = None
        self.playerNames = None

        # The keys for movement must go UP, DOWN, LEFT, RIGHT in the following list.
        self.player_keys = [[Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right],
                            [Qt.Key_W,  Qt.Key_S,    Qt.Key_A,    Qt.Key_D],
                            [Qt.Key_8,  Qt.Key_5,    Qt.Key_4,    Qt.Key_6],
                            [Qt.Key_I,  Qt.Key_K,    Qt.Key_J,    Qt.Key_L]
                            ]

        # object for players points
        self.points = Points()

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

        buttonAbout = QPushButton("ABOUT", self)
        buttonAbout.setStyleSheet(buttonStyle)
        layout.addWidget(buttonAbout, 2, 0)
        buttonAbout.clicked.connect(lambda: self.aboutWindow(layout))

        buttonQuit = QPushButton("QUIT", self)
        buttonQuit.setStyleSheet(buttonStyle)
        layout.addWidget(buttonQuit, 3, 0)
        buttonQuit.clicked.connect(QApplication.instance().quit)

        checkBox = QCheckBox(self)
        checkBox.setChecked(True)
        checkBox.setText("SOUND")
        checkBoxStyle = 'QCheckBox {background-color: transparent; color: red; font: 10pt, Consoles; font-size:15px; ' \
                        'height:48px; width: 120px} '
        checkBox.setStyleSheet(checkBoxStyle)
        layout.addWidget(checkBox, 4, 0)
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
        comboBoxPlayer.addItem("4")
        layout.addWidget(comboBoxPlayer, 0, 2)

        labelEnemies = QLabel()
        labelEnemies.setText("Number of enemies")
        labelEnemies.setStyleSheet(labelStyle)
        layout.addWidget(labelEnemies, 1, 0)

        comboBoxEnemy = QComboBox()
        comboBoxEnemy.setStyleSheet(comboBoxStyle)
        for i in range(16):
            comboBoxEnemy.addItem(str(i+1))
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

        self.enemyThread = EnemyThread()
        for enemy in self.enemiesList:
            self.enemyThread.add_enemy(enemy)

        self.enemyThread.enemy_signal.connect(self.methodMovingEnemy)
        self.enemyThread.enemyStart()

    def __init_ui__(self, layout, number_of_players, number_of_enemies, player_names):
        tableFrame = QFrame()
        mapFrame = QFrame()

        mapFrame.setFrameShape(QFrame.NoFrame)
        mapFrame.setLineWidth(0)
        tableFrame.setFrameShape(QFrame.NoFrame)
        tableFrame.setLineWidth(0)

        tableGrid = QGridLayout()
        mapGrid = QGridLayout()

        tableFrame.setLayout(tableGrid)
        mapFrame.setLayout(mapGrid)
        layout.addWidget(tableFrame, 0, 0)
        layout.addWidget(mapFrame, 0, 1)

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

            #list of all players which play current game
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
                    scaledPix = self.block.scaled(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                  int(mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scaledPix)
                    self.map_wall_labels.append(label)

                elif self.map.map_matrix[i][j] == -4:  # gate
                    scaledPix = self.gatePix.scaled(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                    int(mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scaledPix)
                    self.map_fence_labels.append(label)

                elif self.map.map_matrix[i][j] == 1:  # points
                    scaledPix = self.pointPix.scaled(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                     int(mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scaledPix)
                    self.map_point_labels.append(label)
                    self.map_point_label_row.append(i)
                    self.map_point_label_column.append(j)

                mapGrid.addWidget(label, i, j, Qt.AlignCenter)

        self.playerList = []                # list of players
        self.playerRotationList = []        # list of players rotation
        self.enemiesList = []               # list od enemies

        enemyCounter = 1

        player_counter = 0

        for i in range(len(self.map.map_matrix)):
            for j in range(len(self.map.map_matrix[0])):

                graphScene = QGraphicsScene()
                graphView = QGraphicsView(graphScene)
                label = QLabel()

                if self.map.map_matrix[i][j] == -1 and len(self.playerList) < int(number_of_players):  # start position of Pac-man
                    if player_counter == 0:
                        self.moviePlayer = QMovie('Player1.gif', QByteArray(), self)
                    elif player_counter == 1:
                        self.moviePlayer = QMovie('Player2.gif', QByteArray(), self)
                    elif player_counter == 2:
                        self.moviePlayer = QMovie('Player3.gif', QByteArray(), self)
                    elif player_counter == 3:
                        self.moviePlayer = QMovie('Player4.gif', QByteArray(), self)

                    player_counter += 1

                    self.moviePlayer.setScaledSize(QSize(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                         int(mapFrame.width() / len(self.map.map_matrix))))
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

                    self.map.map_matrix[i][j] = len(self.playerList) + 2    # Setting players on the map
                    mapGrid.addWidget(graphView, i, j, Qt.AlignCenter)

                elif self.map.map_matrix[i][j] == -2 and enemyCounter <= int(number_of_enemies):  # start position of enemy

                    enemyCounter += 1
                    scalePix = self.pix1.scaled(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                int(mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scalePix)

                    self.map.map_matrix[i][j] = 7                       # Setting enemies on the map
                    self.enemiesList.append(label)                      # put enemy in list of enemies
                    mapGrid.addWidget(label, i, j, Qt.AlignCenter)

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

                rect = self.playerList[i].geometry()

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
                self.map_grid.itemAtPosition(self.map_point_label_row[j], self.map_point_label_column[j]).setGeometry(QRect(0, 0, 0, 0))

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
                break
        player_label.setGeometry(rect)

    def methodMovingEnemy(self):
        enemies = self.enemyThread.get_enemies()
        for i in range(len(enemies)):
            rect = self.enemiesList[i].geometry()
            self.enemiesList[i].setGeometry(rect.x() - 5, rect.y(), rect.width(), rect.height())

    def backWindow(self, layout):
        self.enemyThread.enemyDie()
        self.initWindow(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
