import pygame
from game import Game

if __name__ == "__main__":
    pygame.init()
    game = Game()
    command = game.controller.get_keyboard_command()
    while game.isRunning():
        game.update(command)

    pygame.quit()