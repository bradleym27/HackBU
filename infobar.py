
import pygame
from pygame.locals import *
from text import Text


class HUD(object):

    def __init__(self, screen):
        self.screen = screen
        self.bgColor = (150, 150, 150)
        self.height = 70 # height above bottom (y = 960)
        self.text = Text(0,960, str(0))

    def draw(self):
        self.text.draw(self.screen)
        pass


