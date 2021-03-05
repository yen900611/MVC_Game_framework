import math
from os import path

import pygame
from setting import *


class PygameView():
    def __init__(self, game_info = GAME_INFO):
        pygame.display.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.address = "GameView"
        self.font = pygame.font.Font(pygame.font.match_font(font_type, bold=True), charactor_size)

        # loading all image when initial
        if game_info != None and "images" in game_info.keys():
            self.image_dict = self._loading_image(game_info["images"])

    def _loading_image(self, dict):
        result = {}
        for file_name in dict:
            image = pygame.image.load(path.join(IMAGE_DIR, file_name))
            result[file_name]=image
            pass
        return result

    def draw(self, object_imformation = OBJECT_DICT):
        '''
        每個frame呼叫一次，把角色畫在螢幕上
        :param all_sprite:
        :return:
        '''
        object_imformation = self._check_game_object_information(object_imformation)
        for game_object in object_imformation["game_object"]:
            if game_object["type"] == "image":
                if "angle" in game_object.keys():
                    image = pygame.transform.rotate(pygame.transform.scale(self.image_dict[game_object["image"]], game_object["size"]), (game_object["angle"]* 180 / math.pi) % 360)
                    rect = image.get_rect()
                    rect.center = game_object["coordinate"]
                    self.screen.blit(image, rect)

                else:
                    self.screen.blit(pygame.transform.scale(self.image_dict[game_object["image"]], game_object["size"]), game_object["coordinate"])
            elif game_object["type"] == "rectangle":
                pygame.draw.rect(self.screen, game_object["color"],
                                 pygame.Rect(game_object["coordinate"], game_object["size"]))
                pass
            elif game_object["type"] == "vertices":
                pygame.draw.polygon(self.screen, game_object["color"], game_object["vertices"])
                pass
            else:
                pass
            pass

    def draw_screen(self):
        '''draw background'''
        self.screen.fill(BLACK)
        pass

    def flip(self):
        pygame.display.flip()

    def draw_information(self, surf, color,text, x, y):
        text_surface = self.font.render(text , True , color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surf.blit(text_surface , text_rect)

    def _check_game_object_information(self, data: dict):
        if data == None:
            data = {}
            data["game_object"] = []
            return data
        if "game_object" in data.keys():
            for game_object in data["game_object"]:
                if ("name" or "type" or "coordinate") not in game_object.keys():
                    data["game_object"].remove(game_object)
                else:
                    if game_object["type"] == "image":
                        if "image" not in game_object.keys():
                            data["game_object"].remove(game_object)
                    elif game_object["type"] == "rectangle":
                        if ("size" or "color") not in game_object.keys():
                            data["game_object"].remove(game_object)
                    elif game_object["type"] == "vertices":
                        if "vertices" not in game_object.keys():
                            data["game_object"].remove(game_object)
                    else:
                        data["game_object"].remove(game_object)
        else:
            data["game_object"] = []

        return data