import time
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QObject


class EnemyThread(QObject):
    enemy_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(EnemyThread, self).__init__(parent)

        self.enemies = []                                       # list of enemies
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

    def rem_enemy(self, enemy):                 # we need this method for eating enemies
        self.enemies.remove(enemy)

    def get_enemies(self):
        return self.enemies

    @pyqtSlot()
    def __enemyRun__(self):
        while not self.isEnemyDie:
            self.enemy_signal.emit("Enemy")
            time.sleep(0.05)
