import pygame
import config

class Piece(pygame.sprite.Sprite):
    def __init__(self, image, x,y, player):
        super().__init__()
        self.pos_fix=config.border+config.margin+config.piece_fix
        self.image=image
        self.col=x
        self.row=y
        self.update(self.col, self.row)
        self.player=player
        self.king=False
            
    def update(self, x,y):
        self.rect=self.image.get_rect(topleft=(self.pos_fix+x*config.piece_size, 
                                               self.pos_fix+y*config.piece_size))

    def become_king(self, image):
        self.king=True
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, self.rect)