
# Modification date: Mon Jun 26 17:56:00 2023

# Production date: Sun Sep  3 15:43:51 2023

import pygame
pygame.init()

class Road:
    def __init__(self, x, y, genislik, yukseklik, uzaklik):
        self.x, self.y, self.genislik, self.yukseklik, self.uzaklik = x, y, genislik, yukseklik, uzaklik
        #x ve y sol alt noktasının koordinatlarıdır.