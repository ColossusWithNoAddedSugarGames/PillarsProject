import pygame
import math


class HexagonGen(object):
    def __init__(self,edge_length):
        self.edge_length = edge_length

    property

    def col_width(self):
        return self.edge_length * 3

    property

    def row_height(self):
        return math.sin(math.pi / 3) * self.edge_length

    def __call__(self, row, col):
        x = (col + 0.5 * (row % 2)) * self.col_width
        y = row * self.row_height
        for angle in range(0,360,60):
            x += math.cos(math.radians(angle)) * self.edge_length
            y += math.cos(math.radians(angle)) * self.edge_length
            yield x
            yield y

