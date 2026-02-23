import pygame
import config

class Piece(pygame.sprite.Sprite):
    
    textures={}
    @classmethod
    def set_textures(cls, textures):
        cls.textures=textures

    def __init__(self, color, col, row, player):
        super().__init__()
        self.pos_fix = config.border + config.margin + config.piece_fix
        self.color=color
        self.texture = self.textures[self.color]
        self.col = col
        self.row = row
        self.direction = -1 if player==1 else 1
        self.promotion_row = 0 if player==1 else config.board_size-1
        self.king=False
        self.update(self.col, self.row)
            
    
    def become_king(self):
        self.king = True
        self.texture = self.textures[f"king-{self.color}"]

    def update(self, col,row):
        self.col = col
        self.row = row
        self.rect = self.texture.get_rect(topleft=(self.pos_fix + col * config.piece_size, 
                                               self.pos_fix + row * config.piece_size))
        if self.promotion_row == row:
            self.become_king()

    def draw(self, screen):
        screen.blit(self.texture, self.rect)