import os
import sys

from PyQt5.QtCore import QByteArray, Qt
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QSizePolicy, QPushButton, QScrollArea


class MainWindow(QWidget, QGridLayout):         # definicija kalse
    def __init__(self, grid):                   # konstruktor
        super().__init__()
        initUI(self, grid)                      # metoda koja se poziva inicijalno...prizak pocetnog menija


def initUI(self, grid):

    # postavljanje dimenzija prozora,naslova i slike ikonice i boje pozadine..inicijalno se posatvlja
    self.setGeometry(200, 200, 700, 700)
    self.setWindowTitle('Pac-Man')
    absolutePath = os.path.dirname(__file__)
    picturePath = os.path.join(absolutePath, 'Pictures/icon.jpg')
    self.setWindowIcon(QIcon(picturePath))
    QWidget.setStyleSheet(self, "background-color:black")

    #svaki put kada predjem na glavnu stranu moram je update-ovati
    while grid.count() > 0:
        item = grid.takeAt(0)

        if not item:
            continue

        w = item.widget()
        if w:
            w.deleteLater()

    # funkcija za postavljanje gif animacije
    animation_gif(self, grid)

    # funckija za dodavanje button-a glavnog menija
    add_main_buttons(self, grid)

    # postavljam grid na widget
    self.setLayout(grid)

    #sluzi da nam se prikaze prozor
    self.show()


def animation_gif(self, grid):
    movie_screen = QLabel()
    # expand and center the label
    #movie_screen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    movie_screen.setAlignment(Qt.AlignCenter)

    absolutePath = os.path.dirname(__file__)
    picturePath = absolutePath[0:len(absolutePath)-14:1] + '/Pictures/pacmanGif.gif'
    self.movie = QMovie(picturePath, QByteArray(), self)
    #self.movie.setCacheMode(QMovie.CacheAll)
    self.movie.setSpeed(100)
    movie_screen.setMovie(self.movie)

    grid.addWidget(movie_screen, 1, 0, 1, 1)

    self.movie.start()



def add_main_buttons(self, grid):
    button_style = 'QPushButton {background-color: transaprent; color: red; font: 10pt, Consolas; fon-size:36px; height:48px; width: 120px}'
    btn_newgame = QPushButton("NEW GAME", self)
    btn_newgame.setStyleSheet(button_style)

    btn_options = QPushButton("OPTIONS", self)
    btn_options.setStyleSheet(button_style)
    btn_options.clicked.connect(lambda: options_update(self, grid))

    btn_about = QPushButton("ABOUT", self)
    btn_about.setStyleSheet(button_style)
    btn_about.clicked.connect(lambda: about_update(self, grid))

    btn_quit = QPushButton("QUIT", self)
    btn_quit.setStyleSheet(button_style)
    btn_quit.clicked.connect(QApplication.instance().quit)

    grid.addWidget(btn_newgame, 2, 0, 1, 1)
    grid.addWidget(btn_options, 3, 0, 1, 1)
    grid.addWidget(btn_about, 4, 0, 1, 1)
    grid.addWidget(btn_quit, 5, 0, 1, 1)


def about_update(self, grid):

    # brisanje objekata grid-a
    while grid.count() > 0:
        item = grid.takeAt(0)

        if not item:
            continue

        w = item.widget()
        if w:
            w.deleteLater()


    documenation_file = open('about.txt', 'r')

    label = QLabel();
    informations = ""
    for i in documenation_file.readlines():
        informations += i

    label.setText(informations)
    label.setStyleSheet(
        'QLabel {background-color: transparent; color: red; font: 10pt, Consolas; height:48px; width: 120px}')
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
        'QPushButton {background-color: transparent; color: red; font: 10pt, Consolas; height:48px; width: 120px}')
    grid.addWidget(btn_back)
    btn_back.clicked.connect(lambda: initUI(self, grid))


def options_update(self, grid):
    # brisanje objekata grid-a
    while grid.count() > 0:
        item = grid.takeAt(0)

        if not item:
            continue

        w = item.widget()
        if w:
            w.deleteLater()

    style = 'QPushButton {background-color: transparent; color: red; font: 10pt, Consolas; height:48px; width: 120px}'

    label_options = QLabel("OPTIONS",self);
    label_options.setStyleSheet(style)
    label_options.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    label_options.setAlignment(Qt.AlignHCenter)
    grid.addWidget(label_options)

    label_sound = QLabel("SOUND:",self)
    label_sound.setStyleSheet(style)
    label_sound.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    label_sound.setAlignment(Qt.AlignLeft)
    grid.addWidget(label_sound)


    btn_back = QPushButton("BACK", self)
    btn_back.setStyleSheet(style)
    grid.addWidget(btn_back)
    btn_back.clicked.connect(lambda: initUI(self, grid))


if __name__ == '__main__':
    app = QApplication(sys.argv)        # inicijalizacija aplikacije..uvek ide
    grid = QGridLayout()                # pram grid u koji cu da smestam sve objekte(slike,gif,dugmad,labele)
    interface = MainWindow(grid)        # pravim objekat tipa klase koja sluzi za inicijalizaciju prozora.
                                        # Kao parametar mi je grid koji ce mi biyti u tom prozoru
    sys.exit(app.exec_())               # Izlazak iz aplikacije....uvek ide
