import pygame
import math
import Pillars_HexagonGen
import aggdraw

def main():
        image = ('RGB', (250,250), 'white')
        draw = pygame.draw(image)
        hexagongenerator = Pillars_HexagonGen(40)
        for row in range(7):
            colour = row * 10, row * 20, row * 30
            for col in range(2):
                hexagon = hexagongenerator(row, col)
                draw.polygon(list(hexagon), Brush(colour))
            draw.flush()
            draw.show()