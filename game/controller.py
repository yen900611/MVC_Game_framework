import pygame

class EventController():
    def __init__(self):
        self.running = True
        pass

    def get_keyboard_command(self):
        """
        Get the command according to the pressed key command
        """
        pass

    def is_running(self):
        """ Handle the event from window , mouse or button.

        :return: Bool,False means game closed
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.running = False

        return self.running

    def update(self):
        pass


