from os import path
WIDTH = 450
HEIGHT = 600
FPS = 30
font_type = "arial"
charactor_size = 17

'''Color'''
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
RED = (255,0,0)

'''data path'''
IMAGE_DIR = path.join(path.dirname(__file__),"image")

'''game object example, for game view to draw'''
OBJECT_DICT = {
    # "scene":{},
    "game_object":[
        {"type":"image",
         "name":"car",
         "coordinate":(100,200),
         "size":(50,50),
         "image":"car_01.png",
         "angle":60},
        {"type":"rectangle",
         "name":"ball",
         "coordinate":(50,90),
         "size":(5,5),
         "color":(0,0,230)},
        {"type":"vertices",
         "name":"wall",
         "coordinate":(80,60),
         "color":(180,0,0),
         "vertices":[(10,1),(3,1),(3,20),(10,20)]
         }
    ]
}

'''object imformation for game view to initial, include all image name usually'''
GAME_INFO = {
    "images": ["car_01.png"]
}
