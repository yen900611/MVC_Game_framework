from playingMode import PlayingMode
from controller import EventController
from gameView import PygameView

class Game:
    def __init__(self):
        self.gamecore = PlayingMode()
        self.view = PygameView()
        self.controller = EventController()
        self.gameObject = None
        pass

    def get_player_scene_info(self):
        pass

    def update(self):
        cmds = self.controller.get_keyboard_command()
        self.gameObject = self.gamecore.update(cmds)
        self.draw(self.get_game_progress())

    def reset(self):

        pass

    def isRunning(self):
        if self.gamecore.running == False:
            self.controller.running = False
        running = self.controller.is_running()
        return running

    def draw(self,object):
        self.view.draw(object)
        self.view.flip()

    def get_scene_info(self):
        """
        Get the scene information
        """
        pass

    def get_game_info(self):
        """
        Get the scene and object information for drawing on the web
        """
        pass

    def get_game_progress(self):
        """
        Get the position of game objects for drawing on the web
        """
        object_dict = {
            "scene": {},
            "game_object": [
                {"type": "image",
                 "name": "car",
                 "coordinate": (10, 20),
                 "size": (50, 50),
                 "image": "car1.png",
                 "angle": 90},
                {"type": "rectangle",
                 "name": "ball",
                 "coordinate": (50, 90),
                 "size": (5, 5),
                 "color": (0, 0, 230)},
                {"type": "vertices",
                 "name": "wall",
                 "coordinate": (80, 60),
                 "color": (180, 0, 0),
                 "vertices": [(10, 1), (3, 1), (3, 20), (10, 20)]
                 }
            ]
        }
        return object_dict
        pass

    def get_game_result(self):
        """
        Get the game result for the web
        """
        pass
