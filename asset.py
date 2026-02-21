import pygame

class AssetManager():
    def __init__(self):
        self.textures = {}
    
    def load_image(self, name):
        img=pygame.image.load(f"imgs/{name}.png").convert_alpha()
        self.textures[name]=img
        

    def load_pieces(self):
        self.load_image("red")
        self.load_image("black")
        self.load_image("king-red")
        self.load_image("king-black")
    
    def get_image(self, name, size=None):
        img=self.textures[name]
        if size:
            img=pygame.transform.scale(img, (size, size))
        return img