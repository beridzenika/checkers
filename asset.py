import pygame

class AssetManager():
    def __init__(self):
        self.textures = {}
        self.load_pieces()
    
    def load_image(self, name, path):
        img=pygame.image.load(path).convert_alpha()
        self.textures[name]=img
        

    def load_pieces(self):
        self.load_image("red","imgs/red.png")
        self.load_image("black","imgs/black.png")
        self.load_image("king-red","imgs/crown-red.png")
        self.load_image("king-black","imgs/crown-black.png")
    
    def get_image(self, name, size=None):
        img=self.textures[name]
        if size:
            img=pygame.transform.scale(img, (size, size))
        return img