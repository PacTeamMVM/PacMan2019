import os
import sys
import random

from AI import Enemy


class EnemyController:

    def __init__(self, map_matrix, number_of_enemies):

        super().__init__()

        # Matrix that defines the map's structure (walls, starting position, etc.)
        self.map_matrix = map_matrix

        # List of enemies
        self.enemies = []
        for i in range(number_of_enemies):
            color = Enemy.get_next_color()
            self.enemies.append(Enemy.Enemy(color))

    def init_enemies(self):

        # -2 / enemy start pos
        index = 0
        for i in range(len(self.map_matrix)):
            for j in range(len(self.map_matrix[i])):
                if self.map_matrix[i][j] == -2:

                    self.enemies[index].y = i
                    self.enemies[index].x = j
                    self.map_matrix[i][j] = 3

                    index += 1

                    if index >= len(self.enemies):
                        return

    def move_enemies(self):

        for enemy in self.enemies:
            if self.__direction_available(enemy):
                enemy.move()

        return

    def __direction_available(self, enemy):

        # -3 / walls

        if enemy.direction == 1:
            if enemy.x - 1 < 0 or self.map_matrix[enemy.y][enemy.x - 1] == -3:
                return False
            else:
                return True

        if enemy.direction == 2:
            if enemy.x + 1 >= len(self.map_matrix[0]) or self.map_matrix[enemy.y][enemy.x + 1] == -3:
                return False
            else:
                return True

        if enemy.direction == 3:
            if enemy.y - 1 < 0 or self.map_matrix[enemy.y - 1][enemy.x] == -3:
                return False
            else:
                return True

        if enemy.direction == 4:
            if enemy.y + 1 >= len(self.map_matrix) or self.map_matrix[enemy.y + 1][enemy.x] == -3:
                return False
            else:
                return True

        return True

    def change_enemy_direction(self):

        return
