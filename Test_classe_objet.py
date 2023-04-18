import pygame
from pygame.locals import *
from random import *
from math import * 

class Objet:
    
    def __init__(self, image, pos_x=0, pos_y=0):
        self.image = pygame.image.load(image)
        self.long = self.image.get_width
        self.haut = self.image.get_height
        self.x = pos_x
        self.y = pos_y


balle = Objet("random-png.png")
