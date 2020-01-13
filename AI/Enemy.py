import os
import sys
import random


class Enemy:

    def __init__(self, color):

        super().__init__()
        random.seed(420)

        # Enemy position coordinates
        self.x = -1
        self.y = -1

        # Direction of movement
        # 0 - Standing still
        # 1 - Left
        # 2 - Right
        # 3 - Up
        # 4 - Down
        self.direction = 0

        # Determines if the enemy is eatable
        self.eatable = False

        # Color of the enemy
        # Red - #ea1414
        # Orange - #fe8b0c
        # Cyan - #07eded
        # Pink - #dd7fb1
        #
        # Ghost White - #ffffff
        # Ghost Blue - #0412b7
        self.color = color

        # Determines after which amount of steps shall the enemy change direction
        # If this value reaches 0, the enemy shall change direction
        self.direction_changer = random.randrange(1, 9)

    def move(self):

        if self.direction == 1:
            self.x -= 5
        elif self.direction == 2:
            self.x += 5
        elif self.direction == 3:
            self.y -= 5
        elif self.direction == 4:
            self.x += 5

        self.direction_changer -= 1

        if self.direction_changer <= 0:
            self.change_dir()
            self.direction_changer = random.randrange(1, 9)

    def change_dir(self):
        self.direction = random.randrange(1, 4)


# For the static color assignment of the enemy
# Red - #ea1414
# Orange - #fe8b0c
# Cyan - #07eded
# Pink - #dd7fb1
#
# Ghost White - #ffffff
# Ghost Blue - #0412b7
next_color = '#ea1414'


def get_next_color():
    if Enemy.next_color == '#ea1414':
        Enemy.next_color = '#fe8b0c'
        return '#fe8b0c'
    elif Enemy.next_color == '#fe8b0c':
        Enemy.next_color = '#07eded'
        return '#07eded'
    elif Enemy.next_color == '#07eded':
        Enemy.next_color = '#dd7fb1'
        return '#dd7fb1'
    else:
        Enemy.next_color = '#ea1414'
        return '#ea1414'
