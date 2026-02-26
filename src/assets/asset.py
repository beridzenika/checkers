from pathlib import Path
import pygame

BASE_DIR = Path(__file__).resolve().parent
IMG_DIR = BASE_DIR / "imgs"

class AssetManager():
    def __init__(self):
        self.textures = {}
    
    def load_image(self, name, size=None):
        path = IMG_DIR / f"{name}.png"
        img=pygame.image.load(str(path)).convert_alpha()
        if size:
            img=pygame.transform.scale(img, (size, size))
        self.textures[name]=img
        

    def load_pieces(self, size):
        self.load_image("red", size)
        self.load_image("black", size)
        self.load_image("king-red", size)
        self.load_image("king-black", size)

    def get_image(self, name, size=None):
        img=self.textures[name]
        if size:
            img=pygame.transform.scale(img, (size, size))
        return img