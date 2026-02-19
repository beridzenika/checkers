import pygame

class Piece(object):
    def __init__(self, image, x,y):
        self.image=image
        self.rect=self.image.get_rect(topleft=(x, y))
    
    def update(self, x,y):
        self.rect=self.image.get_rect(topleft=(x,y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)