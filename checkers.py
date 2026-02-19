import pygame
import config
from asset import AssetManager
from piece import Piece

class Checkers(object):
    def __init__(self):
        self.pos_fix=config.border+config.margin+config.piece_fix
        assets = AssetManager()

        self.checker_size=config.piece_size-2*config.piece_fix
        self.red=assets.get_image("red", self.checker_size)
        self.black=assets.get_image("black", self.checker_size)
        self.pieces = []
        

    def set_game(self, player):
        if(player=="red"):
            p2=self.red
            p1=self.black
        else:
            p2=self.black
            p1=self.red
        for i in range(config.board_size):
            for j in range(config.board_size):
                if (i+j)%2==1:
                    if i<3:
                        self.pieces.append(Piece(p1, self.pos_fix+j*config.piece_size, self.pos_fix+i*config.piece_size))    
                    elif i>=5:
                        self.pieces.append(Piece(p2, self.pos_fix+j*config.piece_size, self.pos_fix+i*config.piece_size))
    
    def draw(self, screen):
        for piece in self.pieces:
            piece.draw(screen)

    def update(self, x,y):
        pass
    