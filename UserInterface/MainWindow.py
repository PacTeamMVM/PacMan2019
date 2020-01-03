import os
import sys
import winsound

from PyQt5.QtCore import QByteArray, Qt, QSize
from PyQt5.QtGui import QIcon, QMovie, QPixmap
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QLabel, QPushButton, QCheckBox, QSizePolicy, \
    QScrollArea, QComboBox, QLineEdit, QFrame
from PyQt5.uic.Compiler.qtproxies import QtGui, QtCore

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

        #dodao
        self.pix1 = QPixmap('skull2.png')
        self.pix2 = QPixmap('skull1.png')
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.key_notifier = KeyNotifier()

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

        comboBox = QComboBox()
        comboBox.setStyleSheet(comboBoxStyle)
        comboBox.addItem("1")
        comboBox.addItem("2")
        comboBox.addItem("4")
        layout.addWidget(comboBox, 0, 2)

        labelPlayers = QLabel()
        labelPlayers.setText("First player")
        labelPlayers.setStyleSheet(labelStyle)
        layout.addWidget(labelPlayers, 1, 0)

        textBoxFirst = QLineEdit()
        textBoxFirst.setStyleSheet(textBoxStyle)
        layout.addWidget(textBoxFirst, 2, 0)

        labelPlayers = QLabel()
        labelPlayers.setText("Second player")
        labelPlayers.setStyleSheet(labelStyle)
        layout.addWidget(labelPlayers, 3, 0)

        textBoxSecond = QLineEdit()
        textBoxSecond.setStyleSheet(textBoxStyle)
        layout.addWidget(textBoxSecond, 4, 0)

        labelPlayers = QLabel()
        labelPlayers.setText("Third player")
        labelPlayers.setStyleSheet(labelStyle)
        layout.addWidget(labelPlayers, 5, 0)

        textBoxThird = QLineEdit()
        textBoxThird.setStyleSheet(textBoxStyle)
        layout.addWidget(textBoxThird, 6, 0)

        labelPlayers = QLabel()
        labelPlayers.setText("Fourth player")
        labelPlayers.setStyleSheet(labelStyle)
        layout.addWidget(labelPlayers, 7, 0)

        textBoxFourth = QLineEdit()
        textBoxFourth.setStyleSheet(textBoxStyle)
        layout.addWidget(textBoxFourth, 8, 0)

        buttonBack = QPushButton("BACK", self)
        buttonBack.setStyleSheet(
            'QPushButton {background-color: transparent; color: red; font: 10pt, Consoles; height:48px; width: 120px}')
        layout.addWidget(buttonBack, 9, 0)
        buttonBack.clicked.connect(lambda: self.initWindow(layout))

        buttonBack = QPushButton("PLAY", self)
        buttonBack.setStyleSheet(
            'QPushButton {background-color: transparent; color: red; font: 10pt, Consoles; height:48px; width: 120px}')
        layout.addWidget(buttonBack, 9, 2)
        buttonBack.clicked.connect(lambda: self.maze(layout))

        self.setLayout(layout)

    def maze(self, layout):
        cleanGrid(layout)
        self.setWindowState(Qt.WindowMaximized)

        '''labelPlayer1 = QLabel()
        labelPlayer1.setText("Player1:")
        labelPlayer2 = QLabel()
        labelPlayer2.setText("Player2:")
        labelPlayer3 = QLabel()
        labelPlayer3.setText("Player3:")
        labelPlayer4 = QLabel()
        labelPlayer4.setText("Player4:")

        mapLayout = QGridLayout()
        
        layout.addItem(mapLayout)'''

        #layout.addChildLayout(mapLayout)
        #layout
        #layout.addChildWidget(labelPlayer1,0,0)
        #layout.addWidget(labelPlayer1, 0, ,0, 10, 10)
        #layout.addChildWidget(labelPlayer2, 1,1)
        #layout.addChildWidget(labelPlayer3,2,2)
        #layout.addChildWidget(labelPlayer4,3,3)

        self.__init_ui__(layout)

        self.key_notifier.key_signal.connect(self.__update_position__)
        self.key_notifier.start()

    def __init_ui__(self, layout):

        # layout = QGridLayout()

        tableFrame = QFrame()
        mapFrame = QFrame()

        mapFrame.setFrameShape(QFrame.NoFrame)
        mapFrame.setLineWidth(0)

        tableGrid = QGridLayout()
        mapGrid = QGridLayout()

        tableFrame.setLayout(tableGrid)
        mapFrame.setLayout(mapGrid)

        layout.addWidget(tableFrame, 0, 0)
        layout.addWidget(mapFrame, 0, 1)

        tableGrid.addWidget(QLabel("nesto"), 0, 0)

        self.map = Map()
        self.playerList = []

        enemyCounter = 1
        for i in range(len(self.map.map_matrix)):
            for j in range(len(self.map.map_matrix[0])):

                label = QLabel()

                if self.map.map_matrix[i][j] == -3: # zidovi

                    pixmap = QPixmap('block.png')
                    scaled_pixmap = pixmap.scaled(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                  int(mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scaled_pixmap)

                elif self.map.map_matrix[i][j] == -4: # ograda

                    pixmap = QPixmap('gate.png')
                    scaled_pixmap = pixmap.scaled(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                  int(mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scaled_pixmap)

                elif self.map.map_matrix[i][j] == -2:  # pocetna pozicija neprijatelja

                    pixmap = QPixmap('skull' + str(enemyCounter) + '.png')
                    enemyCounter += 1
                    scaled_pixmap = pixmap.scaled(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                  int(mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scaled_pixmap)


                elif self.map.map_matrix[i][j] == 1: # poeni

                    pixmap = QPixmap('point.png')
                    scaled_pixmap = pixmap.scaled(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                  int(mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scaled_pixmap)

                elif self.map.map_matrix[i][j] == 2: # veliki poeni

                    pixmap = QPixmap('big_point.png')
                    scaled_pixmap = pixmap.scaled(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                  int(mapFrame.height() / len(self.map.map_matrix)))
                    label.setPixmap(scaled_pixmap)

                # label.setText(str(self.map.map_matrix[i][j]))
                mapGrid.addWidget(label, i, j, Qt.AlignCenter)


        for i in range(len(self.map.map_matrix)):
            for j in range(len(self.map.map_matrix[0])):
                label = QLabel()
                if self.map.map_matrix[i][j] == -1: # pocetna pozicija pacmena

                    movie = QMovie('pacman.gif', QByteArray(), self)
                    movie.setScaledSize(QSize(int(mapFrame.width() / len(self.map.map_matrix[0])),
                                                  int(mapFrame.height() / len(self.map.map_matrix))))
                    movie.setSpeed(100)
                    label.setMovie(movie)
                    movie.start()

                    self.playerList.append(label)
                    mapGrid.addWidget(label, i, j, Qt.AlignCenter)

        self.setLayout(layout)


#        self.label1.setPixmap(pixmap4)
 #       self.label1.setGeometry(100, 40, 20, 20)
#
 #       self.label2.setPixmap(self.pix2)
  #      self.label2.setGeometry(50, 40, 50, 50)

        #layout.addWidget(self.label1)
        #alayout.addWidget(self.label2)

        #self.show()

    def keyPressEvent(self, event):
        self.key_notifier.add_key(event.key())

    def keyReleaseEvent(self, event):
        self.key_notifier.rem_key(event.key())

    def __update_position__(self, key):
        rec1 = self.playerList[0].geometry()
        rec2 = self.playerList[1].geometry()

        if key == Qt.Key_Right:
            self.playerList[0].setGeometry(rec1.x() + 5, rec1.y(), rec1.width(), rec1.height())
        elif key == Qt.Key_Down:
            self.playerList[0].setGeometry(rec1.x(), rec1.y() + 5, rec1.width(), rec1.height())
        elif key == Qt.Key_Up:
            self.playerList[0].setGeometry(rec1.x(), rec1.y() - 5, rec1.width(), rec1.height())
        elif key == Qt.Key_Left:
            self.playerList[0].setGeometry(rec1.x() - 5, rec1.y(), rec1.width(), rec1.height())

        if key == Qt.Key_D:
            self.playerList[1].setGeometry(rec2.x() + 5, rec2.y(), rec2.width(), rec2.height())
        elif key == Qt.Key_S:
            self.playerList[1].setGeometry(rec2.x(), rec2.y() + 5, rec2.width(), rec2.height())
        elif key == Qt.Key_W:
            self.playerList[1].setGeometry(rec2.x(), rec2.y() - 5, rec2.width(), rec2.height())
        elif key == Qt.Key_A:
            self.playerList[1].setGeometry(rec2.x() - 5, rec2.y(), rec2.width(), rec2.height())

    def closeEvent(self, event):
        self.key_notifier.die()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
