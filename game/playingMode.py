import pygame
# from setting import *
from setting import FPS


class PlayingMode():
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.all_sprite = pygame.sprite.Group()
        self.address = "GameMode"
        pass

    def update(self,data):
        self.ticks()
        pass

    def ticks(self,fps = FPS):
        self.clock.tick(fps)
