import os
import sys

from PyQt5.QtCore import QByteArray, Qt, QState
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtMultimedia import QSound
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QSizePolicy, QPushButton, QScrollArea, \
    QCheckBox, QDesktopWidget

sound = QSound("music.wav")


class MainWindow(QWidget, QGridLayout):
    def __init__(self, grid):
        super().__init__()
        sound.play()
        initUI(self, grid)


def initUI(self, grid):
    self.setGeometry(200, 200, 700, 700)
    self.setWindowTitle('Pac-Man')
    absolutePath = os.path.dirname(__file__)
    picturePath = os.path.join(absolutePath, 'Pictures/icon.jpg')
    self.setWindowIcon(QIcon(picturePath))
    QWidget.setStyleSheet(self, "background-color:black")

    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

    while grid.count() > 0:
        item = grid.takeAt(0)
        if not item:
            continue
        w = item.widget()
        if w:
            w.deleteLater()

    animation_gif(self, grid)
    add_main_buttons(self, grid)
    self.setLayout(grid)
    self.show()


def animation_gif(self, grid):
    movie_screen = QLabel()
    # expand and center the label
    # movie_screen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    movie_screen.setAlignment(Qt.AlignCenter)

    absolutePath = os.path.dirname(__file__)
    picturePath = absolutePath[0:len(absolutePath) - 14:1] + '/Pictures/pacmanGif.gif'
    self.movie = QMovie(picturePath, QByteArray(), self)
    # self.movie.setCacheMode(QMovie.CacheAll)
    self.movie.setSpeed(100)
    movie_screen.setMovie(self.movie)

    grid.addWidget(movie_screen, 1, 0, 1, 1)

    self.movie.start()


def add_main_buttons(self, grid):
    button_style = 'QPushButton {background-color: transparent; color: red; font: 10pt, Consoles; fon-size:36px; ' \
                   'height:48px; width: 120px} '
    btn_newGame = QPushButton("NEW GAME", self)
    btn_newGame.setStyleSheet(button_style)
    btn_newGame.clicked.connect(lambda: newGame_update(self, grid))

    btn_options = QPushButton("OPTIONS", self)
    btn_options.setStyleSheet(button_style)
    btn_options.clicked.connect(lambda: options_update(self, grid))

    btn_about = QPushButton("ABOUT", self)
    btn_about.setStyleSheet(button_style)
    btn_about.clicked.connect(lambda: about_update(self, grid))

    btn_quit = QPushButton("QUIT", self)
    btn_quit.setStyleSheet(button_style)
    btn_quit.clicked.connect(QApplication.instance().quit)

    grid.addWidget(btn_newGame, 2, 0, 1, 1)
    grid.addWidget(btn_options, 3, 0, 1, 1)
    grid.addWidget(btn_about, 4, 0, 1, 1)
    grid.addWidget(btn_quit, 5, 0, 1, 1)


def newGame_update(self, grid):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

    while grid.count() > 0:
        item = grid.takeAt(0)
        if not item:
            continue
        w = item.widget()
        if w:
            w.deleteLater()

    btn_back = QPushButton("BACK", self)
    btn_back.setStyleSheet(
        'QPushButton {background-color: transparent; color: red; font: 10pt, Consoles; height:48px; width: 120px}')
    grid.addWidget(btn_back)
    btn_back.clicked.connect(lambda: initUI(self, grid))


def about_update(self, grid):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

    while grid.count() > 0:
        item = grid.takeAt(0)
        if not item:
            continue
        w = item.widget()
        if w:
            w.deleteLater()

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
    # s.setMinimumHeight(self.height())
    s.setAlignment(Qt.AlignHCenter)
    grid.addWidget(s)
    # s.setWidget(grid)
    s.setWidget(label)
    s.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    btn_back = QPushButton("BACK", self)
    btn_back.setStyleSheet(
        'QPushButton {background-color: transparent; color: red; font: 10pt, Consoles; height:48px; width: 120px}')
    grid.addWidget(btn_back)
    btn_back.clicked.connect(lambda: initUI(self, grid))


def options_update(self, grid):
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())

    while grid.count() > 0:
        item = grid.takeAt(0)

        if not item:
            continue

        w = item.widget()
        if w:
            w.deleteLater()

    style_label = 'QLabel {background-color: transparent; color: red; font: 10pt, Consoles; height:48px; width: 120px}'
    style_button = 'QPushButton {background-color: transparent; color: red; font: 10pt, Consoles;' \
                   ' height:48px; width: 120px}'
    style_checkBox = 'QCheckBox {background-color: transparent; color: red; font: 10pt, Consoles;' \
                     ' height:48px; width: 120px}'

    label_options = QLabel("OPTIONS", self)
    label_options.setStyleSheet(style_label)
    label_options.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    label_options.setAlignment(Qt.AlignHCenter)
    grid.addWidget(label_options)

    '''label_sound = QLabel("SOUND:", self)
    label_sound.setStyleSheet(style_label)
    label_sound.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    label_sound.setAlignment(Qt.AlignLeft)'''

    checkBox = QCheckBox("SOUND", self)
    checkBox.setStyleSheet(style_checkBox)
    checkBox.setChecked(True)
    checkBox.stateChanged.connect(lambda: clickBox(self, checkBox.checkState()))

    grid.addWidget(checkBox)

    btn_back = QPushButton("BACK", self)
    btn_back.setStyleSheet(style_button)
    btn_back.clicked.connect(lambda: initUI(self, grid))
    grid.addWidget(btn_back)

    # grid.addWidget(btn_back, 2, 0, 1, 1)


def clickBox(self, state):
    if state == Qt.Checked:
        sound.play()
    else:
        sound.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    grid = QGridLayout()
    interface = MainWindow(grid)
    sys.exit(app.exec_())
