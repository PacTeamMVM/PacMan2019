from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class PointLabel(QLabel):

    clicked = QtCore.pyqtSignal()

    def __init__(self, big_point_pixmap, parent=None):
        super(PointLabel, self).__init__(parent)
        self.collected = False
        self.collected_big = False
        self.big_point = False
        self.big_point_pixmap = big_point_pixmap

    def paintEvent(self, event):
        super(PointLabel, self).paintEvent(event)
        rect = event.rect()
        painter = QtGui.QPainter(self)
        painter.setBrush(QtGui.QBrush(QtCore.Qt.white))
        painter.setPen(QtGui.QPen(QtCore.Qt.white))

        if self.big_point and not self.collected_big:
            painter.setBrush(QtGui.QBrush(QtCore.Qt.yellow))
            painter.setPen(QtGui.QPen(QtCore.Qt.yellow))
            painter.drawRect(self.width() / 2 - 5, self.height() / 2 - 5, 10, 10)
            #painter.drawEllipse(QPoint(self.width() / 2, self.height() / 2), 3, 3)
            #painter.drawEllipse(0, 0, 5, 5)
            #painter.drawPixmap(rect, self.big_point_pixmap)
        elif not self.collected:
            painter.drawEllipse(QPoint(self.width() / 2, self.height() / 2), 2, 2)

        painter.end()

    def mousePressEvent(self, event):
        event.accept()
        self.clicked.emit()
