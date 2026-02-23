import pygame

class AssetManager():
    def __init__(self):
        self.textures = {}
    
    def load_image(self, name, size=None):
        img=pygame.image.load(f"imgs/{name}.png").convert_alpha()
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