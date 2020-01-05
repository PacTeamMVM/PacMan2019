import os
import sys
import winsound

from PyQt5.QtCore import QByteArray, Qt, QSize
from PyQt5.QtGui import QIcon, QMovie, QPixmap
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QLabel, QPushButton, QCheckBox, QSizePolicy, \
    QScrollArea, QComboBox, QLineEdit, QFrame, QGraphicsView, QGraphicsScene, QTableWidget, QTableWidgetItem, \
    QHeaderView

from Map.key_notifier import KeyNotifier
from Map.Map import Map


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


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.initWindow(layout)

        self.pix1 = QPixmap('skull_enemy.png')
        self.pix2 = QPixmap('skull_friendly.png')
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.key_notifier = None
        self.movie = None

        self.show()
        winsound.PlaySound("music.wav", winsound.SND_LOOP + winsound.SND_ASYNC)

    def initWindow(self, layout):
        self.setGeometry(750, 250, 700, 700)
        self.setWindowTitle("PacMan2020")
        absolutePath = os.path.dirname(__file__)
        picturePath = os.path.join(absolutePath[0:len(absolutePath) - 13:1], 'Pictures/icon.jpg')
        self.setWindowIcon(QIcon(picturePath))
        self.setStyleSheet("background-color:black")

        cleanGrid(layout)
        self.animation(layout)

        buttonStyle = 'QPushButton {background-color: transparent; color: red; font: 10pt, Consoles; fon-size:36px; ' \
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
        checkBoxStyle = 'QCheckBox {background-color: transparent; color: red; font: 10pt, Consoles; fon-size:36px; ' \
                        'height:48px; width: 120px} '
        checkBox.setStyleSheet(checkBoxStyle)
        layout.addWidget(checkBox, 4, 0)
        checkBox.stateChanged.connect(lambda: clickBox(checkBox.checkState()))

        self.setLayout(layout)

    def animation(self, layout):
        movie_screen = QLabel()
        movie_screen.setAlignment(Qt.AlignCenter)
        absolutePath = os.path.dirname(__file__)
        picturePath = absolutePath[0:len(absolutePath) - 14:1] + '/Pictures/pacmanGif.gif'
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
            'QPushButton {background-color: transparent; color: red; font: 10pt, Consoles; height:48px; width: 120px}')
        layout.addWidget(buttonBack, 1, 0)
        buttonBack.clicked.connect(lambda: self.initWindow(layout))

    def newGameWindow(self, layout):
        cleanGrid(layout)
        labelStyle = 'QLabel {background-color: transparent; color: red; font: 10pt, Consoles; height:48px; width: 120px}'
        comboBoxStyle = 'QComboBox {background-color: white; color: red; font: 10pt, Consoles; height:48px; width: 120px}'
        textBoxStyle = 'QLineEdit {background-color: white; color: red; font: 10pt, Consoles; height:48px; width: 120px}'

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
            'QPushButton {background-color: transparent; color: red; font: 10pt, Consoles; height:48px; width: 120px}')
        layout.addWidget(buttonBack, 10, 0)
        buttonBack.clicked.connect(lambda: self.initWindow(layout))

        buttonPlay = QPushButton("PLAY", self)
        buttonPlay.setStyleSheet(
            'QPushButton {background-color: transparent; color: red; font: 10pt, Consoles; height:48px; width: 120px}')
        layout.addWidget(buttonPlay, 10, 2)
        buttonPlay.clicked.connect(lambda: self.maze(layout, comboBoxPlayer.currentText(), comboBoxEnemy.currentText(),
                                                     [textBoxFirst.text(), textBoxSecond.text(), textBoxThird.text(), textBoxFourth.text()]))

        self.setLayout(layout)

    def maze(self, layout, number_of_players, number_of_enemies, player_names):
        cleanGrid(layout)

        self.__init_ui__(layout, number_of_players, number_of_enemies, player_names)
        self.setWindowState(Qt.WindowMaximized)
        self.key_notifier = KeyNotifier()
        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

    def __init_ui__(self, layout, number_of_players, number_of_enemies, player_names):
        winsound.PlaySound(None, winsound.SND_PURGE)
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

        tableStyle = 'QTableWidget {background-color: transparent; color: red; font: 10pt, Consoles; height:48px; width: 120px; }'
        tableWidget = QTableWidget()
        tableWidget.setRowCount(int(number_of_players))
        tableWidget.setColumnCount(3)
        tableWidget.setStyleSheet(tableStyle)
        tableWidget.setHorizontalHeaderLabels(["Name", "Health", "Points"])
        tableGrid.addWidget(tableWidget)

        for i in range(int(number_of_players)):
            nameItem = QTableWidgetItem(str(player_names[i]))
            nameItem.setTextAlignment(Qt.AlignCenter)
            tableWidget.setItem(i, 0, nameItem)
            healthItem = QTableWidgetItem("0")
            healthItem.setTextAlignment(Qt.AlignCenter)
            tableWidget.setItem(i, 1, healthItem)
            pointsItem = QTableWidgetItem("0")
            pointsItem.setTextAlignment(Qt.AlignCenter)
            tableWidget.setItem(i, 2, pointsItem)

        buttonBack = QPushButton("BACK", self)
        buttonBack.setStyleSheet(
            'QPushButton {background-color: transparent; color: red; font: 10pt, Consoles; height:48px; width: 120px}')
        layout.addWidget(buttonBack, 1, 0)
        buttonBack.clicked.connect(lambda: self.initWindow(layout))

        self.map = Map()

        for i in range(len(self.map.map_matrix)):
            for j in range(len(self.map.map_matrix[0])):

                label = QLabel()

                if self.map.map_matrix[i][j] == -3:  # zidovi

                    pixmap = QPixmap('block.png')
                    scaled_pixmap = pixmap.scaled(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                  int(mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scaled_pixmap)

                elif self.map.map_matrix[i][j] == -4:  # ograda

                    pixmap = QPixmap('gate.png')
                    scaled_pixmap = pixmap.scaled(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                  int(mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scaled_pixmap)

                elif self.map.map_matrix[i][j] == 1:  # poeni

                    pixmap = QPixmap('point.png')
                    scaled_pixmap = pixmap.scaled(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                  int(mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scaled_pixmap)

                elif self.map.map_matrix[i][j] == 2:  # veliki poeni

                    pixmap = QPixmap('big_point.png')
                    scaled_pixmap = pixmap.scaled(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                  int(mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scaled_pixmap)

                # label.setText(str(self.map.map_matrix[i][j]))
                mapGrid.addWidget(label, i, j, Qt.AlignCenter)

        self.playerList = []
        self.playerRotationList = []
        enemyCounter = 1
        for i in range(len(self.map.map_matrix)):
            for j in range(len(self.map.map_matrix[0])):

                graphScene = QGraphicsScene()
                graphView = QGraphicsView(graphScene)
                label = QLabel()

                if self.map.map_matrix[i][j] == -1 and len(self.playerList) < int(number_of_players):  # pocetna pozicija pacmena

                    movie = QMovie('pacman.gif', QByteArray(), self)
                    movie.setScaledSize(QSize(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                              int(mapFrame.height() / len(self.map.map_matrix))))
                    movie.setSpeed(100)
                    label.setMovie(movie)
                    label.setAttribute(Qt.WA_NoSystemBackground)
                    movie.start()

                    graphScene.setBackgroundBrush(Qt.black)
                    graphScene.addWidget(label)
                    graphView.setFrameShape(QFrame.NoFrame)
                    graphView.setStyleSheet("background: transparent")
                    graphView.setSceneRect(0, 0, label.width(), label.width())
                    graphView.setFixedSize(label.width(), label.width())

                    self.playerList.append(graphView)
                    self.playerRotationList.append(0)
                    self.map.map_matrix[i][j] = len(self.playerList) + 2

                    mapGrid.addWidget(graphView, i, j, Qt.AlignCenter)

                elif self.map.map_matrix[i][j] == -2 and enemyCounter <= int(number_of_enemies):  # pocetna pozicija neprijatelja

                    pixmap = QPixmap('skull_enemy.png')
                    enemyCounter += 1
                    scaled_pixmap = pixmap.scaled(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                  int(mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scaled_pixmap)

                    self.map.map_matrix[i][j] = 7
                    mapGrid.addWidget(label, i, j, Qt.AlignCenter)

        self.setLayout(layout)

    def keyPressEvent(self, event):
        if self.key_notifier is not None:
            self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        if self.key_notifier is not None:
            self.key_notifier.rem_key(event.key())

    def __update_position__(self, key):

        rec1 = self.playerList[0].geometry()

        # Player 1
        if key == Qt.Key_Right:
            if self.playerRotationList[0] != 0:
                self.playerList[0].rotate(-self.playerRotationList[0])
                self.playerRotationList[0] = 0
            self.playerList[0].setGeometry(rec1.x() + 5, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_Down:
            if self.playerRotationList[0] != 90:
                self.playerList[0].rotate(-self.playerRotationList[0])
                self.playerList[0].rotate(90)
                self.playerRotationList[0] = 90
            self.playerList[0].setGeometry(rec1.x(), rec1.y() + 5, rec1.width(), rec1.height())
        elif key == Qt.Key_Up:
            if self.playerRotationList[0] != -90:
                self.playerList[0].rotate(-self.playerRotationList[0])
                self.playerList[0].rotate(-90)
                self.playerRotationList[0] = -90
            self.playerList[0].setGeometry(rec1.x(), rec1.y() - 5, rec1.width(), rec1.height())
        elif key == Qt.Key_Left:
            if self.playerRotationList[0] != 180:
                self.playerList[0].rotate(-self.playerRotationList[0])
                self.playerList[0].rotate(180)
                self.playerRotationList[0] = 180
            self.playerList[0].setGeometry(rec1.x() - 5, rec1.y(), rec1.width(), rec1.height())

        # Player 2
        if len(self.playerList) > 1:
            rec2 = self.playerList[1].geometry()
            if key == Qt.Key_D:
                self.playerList[1].setGeometry(rec2.x() + 5, rec2.y(), rec2.width(), rec2.height())
            elif key == Qt.Key_S:
                self.playerList[1].setGeometry(rec2.x(), rec2.y() + 5, rec2.width(), rec2.height())
            elif key == Qt.Key_W:
                self.playerList[1].setGeometry(rec2.x(), rec2.y() - 5, rec2.width(), rec2.height())
            elif key == Qt.Key_A:
                self.playerList[1].setGeometry(rec2.x() - 5, rec2.y(), rec2.width(), rec2.height())

    def closeEvent(self, event):
        if self.key_notifier is not None:
            self.key_notifier.die()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
