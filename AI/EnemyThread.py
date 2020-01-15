import time
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QObject

from AI.EnemyValues import EnemyValues


class EnemyThread(QObject):
    enemy_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(EnemyThread, self).__init__(parent)

        self.enemySpeed = 0.075                                 # speed of enemies moving
        self.enemies = []                                       # list of enemies
        self.enemy_values = []
        self.isEnemyDie = False
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.__enemyRun__)

    def enemyStart(self):
        self.thread.start()

    def enemyDie(self):
        self.isEnemyDie = True
        self.enemies.clear()
        self.thread.quit()

    def add_enemy(self, enemy):                 # we need this method for eating enemies
        self.enemies.append(enemy)
        self.enemy_values.append(EnemyValues())

    def rem_enemy(self, enemy):                 # we need this method for eating enemies
        self.enemies.remove(enemy)
        self.enemy_values.remove(self.enemy_values[len(self.enemy_values) - 1])

    def get_enemies(self):
        return self.enemies

    def get_enemy_values(self):
        return self.enemy_values

    def changeEnemySpeed(self, numberLevel):        # high level -> high speed
        if numberLevel <= 1:
            self.enemySpeed = 0.075
        elif numberLevel == 2:
            self.enemySpeed = 0.065
        elif numberLevel == 3:
            self.enemySpeed = 0.06
        elif numberLevel == 4:
            self.enemySpeed = 0.055
        elif numberLevel == 5:
            self.enemySpeed = 0.05
        else:
            self.enemySpeed = 0.04

    @pyqtSlot()
    def __enemyRun__(self):
        while not self.isEnemyDie:
            self.enemy_signal.emit("Enemy")
            time.sleep(0.005)
