import pygame
import config

class Board():
    def __init__(self):
        # self.board=[[0*board_size]*board_size]
        self.pos_fix=config.border+config.margin
        self.border_size=config.piece_size*config.board_size+config.border*2

    def draw(self, screen):
        rec=pygame.Rect(config.margin, config.margin, self.border_size, self.border_size)
        pygame.draw.rect(screen, config.border_color, rec)
        
        for i in range(config.board_size):
            for j in range(config.board_size):
                color = config.white_color if (i+j)%2==0 else config.black_color
                rec=pygame.Rect(self.pos_fix + i*config.piece_size, self.pos_fix + j*config.piece_size, config.piece_size, config.piece_size)
                pygame.draw.rect(screen, color, rec)