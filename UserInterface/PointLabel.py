from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPixmap, QPainterPath
from PyQt5.QtWidgets import QLabel


class PointLabel(QLabel):

    clicked = QtCore.pyqtSignal()

    def __init__(self, big_point_pixmap, parent=None):
        super(PointLabel, self).__init__(parent)
        self.collected = False
        self.collected_big = False
        self.collected_deus_ex = False
        self.big_point = False
        self.deus_ex_heart = False
        self.deus_ex_appearing = False
        self.big_point_pixmap = big_point_pixmap

    def paintEvent(self, event):
        super(PointLabel, self).paintEvent(event)
        rect = event.rect()
        painter = QtGui.QPainter(self)
        painter.setBrush(QtGui.QBrush(QtCore.Qt.white))
        painter.setPen(QtGui.QPen(QtCore.Qt.white))

        if self.deus_ex_heart and not self.collected_deus_ex:
            painter.setBrush(QtGui.QBrush(QtCore.Qt.black))
            if not self.deus_ex_appearing:
               painter.setBrush(QtGui.QBrush(QtCore.Qt.red))
            painter.setPen(QtGui.QPen(QtCore.Qt.red))
            path = QPainterPath()
            path.moveTo(5, 5)
            path.lineTo(5, self.height() / 3)
            path.lineTo(self.width() / 2, self.height() - 5)
            path.lineTo(self.width() - 5, self.height() / 3)
            path.lineTo(self.width() - 5, 5)
            path.lineTo(self.width() - 7, 5)
            path.lineTo(self.width() / 2, self.height() / 2.5)
            path.lineTo(7, 5)
            path.lineTo(5, 5)
            painter.drawPath(path)
        elif self.big_point and not self.collected_big:
            painter.setBrush(QtGui.QBrush(QtCore.Qt.yellow))
            painter.setPen(QtGui.QPen(QtCore.Qt.yellow))
            painter.drawRect(self.width() / 2 - 5, self.height() / 2 - 5, 10, 10)
        elif not self.collected:
            painter.drawEllipse(QPoint(self.width() / 2, self.height() / 2), 2, 2)

        painter.end()

    def mousePressEvent(self, event):
        event.accept()
        self.clicked.emit()
