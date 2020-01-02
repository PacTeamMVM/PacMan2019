import os
import sys


class Map:

    def __init__(self):

        super().__init__()

        # -4 - enemy gate
        # -3 - walls
        # -2 - enemy starting position
        # -1 - player starting position
        #  0 - empty fields
        #  1 - points
        #  2 - big point

        half_map_matrix = [[-3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3],
                           [-3,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -3],
                           [-3,  1, -3, -3, -3, -3,  1, -3, -3, -3, -3, -3,  1, -3],
                           [-3,  2, -3, -3, -3, -3,  1, -3, -3, -3, -3, -3,  1, -3],
                           [-3,  1, -3, -3, -3, -3,  1, -3, -3, -3, -3, -3,  1, -3],
                           [-3,  1,  1,  1,  1,  1, -1,  1,  1,  1,  1,  1,  1,  1],
                           [-3,  1, -3, -3, -3, -3,  1, -3, -3,  1, -3, -3, -3, -3],
                           [-3,  1, -3, -3, -3, -3,  1, -3, -3,  1, -3, -3, -3, -3],
                           [-3,  1,  1,  1,  1,  1,  1, -3, -3,  1,  1,  1,  1, -3],
                           [-3, -3, -3, -3, -3, -3,  1, -3, -3, -3, -3, -3,  0, -3],
                           [ 0,  0,  0,  0,  0, -3,  1, -3, -3, -3, -3, -3,  0, -3],
                           [ 0,  0,  0,  0,  0, -3,  1, -3, -3,  0,  0,  0,  0, -2],
                           [ 0,  0,  0,  0,  0, -3,  1, -3, -3,  0, -3, -3, -3, -4],
                           [-3, -3, -3, -3, -3, -3,  1, -3, -3,  0, -3, -2, -2, -2],
                           [ 0,  0,  0,  0,  0,  0,  1, -3, -3,  0, -3, -2, -2, -2],
                           ]

        self.map_matrix = []
        for i in range(len(half_map_matrix)):

            new = []

            for j in range(len(half_map_matrix[0])):
                new.append(half_map_matrix[i][j])
            for j in range(len(half_map_matrix[0])):
                new.append(half_map_matrix[i][len(half_map_matrix[0]) - j - 1])

            self.map_matrix.append(new)

        for i in range(len(half_map_matrix) - 1):

            new = []

            for j in range(len(half_map_matrix[0])):
                new.append(half_map_matrix[len(half_map_matrix) - i - 2][j])
            for j in range(len(half_map_matrix[0])):
                new.append(half_map_matrix[len(half_map_matrix) - i - 2][len(half_map_matrix[0]) - j - 1])

            self.map_matrix.append(new)

        # for i in range(len(self.map_matrix)):
          #  print(self.map_matrix[i])


map = Map()