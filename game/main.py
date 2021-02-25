import pygame
from game import Game

if __name__ == "__main__":
    pygame.init()
    game = Game()
    pass
    while game.isRunning():
        game.update()

    pygame.quit()