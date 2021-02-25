import pygame
from setting import *

class PlayingMode():
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.match_font("arial", bold=True), 40)
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
