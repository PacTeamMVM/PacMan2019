import time
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QObject

from AI.EnemyValues import EnemyValues


class EnemyThread(QObject):
    enemy_signal = pyqtSignal(int)

    def __init__(self, parent=None):
        super(EnemyThread, self).__init__(parent)

        self.enemySpeed = 0.075                                 # speed of enemies moving
        self.enemy = None                                       # list of enemies
        self.enemy_values = None
        self.slowed_down = 1
        self.index = -1
        self.isEnemyDie = False
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(self.__enemyRun__)

    def enemyStart(self):
        self.thread.start()

    def enemyDie(self):
        self.isEnemyDie = True
        self.thread.quit()

    def assign_enemy(self, enemy):                 # we need this method for eating enemies
        self.enemy = enemy
        self.enemy_values = EnemyValues()

    def get_enemy(self):
        return self.enemy

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

    def slow_down(self, is_slowed):
        if is_slowed:
            self.slowed_down = 5
        else:
            self.slowed_down = 1

    @pyqtSlot()
    def __enemyRun__(self):
        while not self.isEnemyDie:
            self.enemy_signal.emit(self.index)
            time.sleep(0.005 * self.slowed_down)
