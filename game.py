import pygame
import config
from asset import AssetManager
from board import Board

class Game():
    def __init__(self):
        self.board = Board()
        self.board.set_game(config.player)
        self.pos_fix=config.border+config.margin
        self.positions=[]
        self.captures={}

    def draw_selected(self, screen):
        for rec in self.positions:
            pygame.draw.rect(screen, config.select_color, rec)

    def draw(self, screen):
        screen.fill((config.back_color))
        self.board.draw_board(screen)
        self.draw_selected(screen)
        self.board.draw_pieces(screen)

    def handle_click(self, pos):
        col, row = pos
        col=self.pos_to_idx(col)
        row=self.pos_to_idx(row)

        if (col>=0 and col<config.board_size and row>=0 and row<config.board_size):
            if self.board.board[col][row]!=0: #selected a piece
                self.positions=[]
                self.captures={}
                moves=self.board.valid_moves(col,row)
                rec=self.make_rec(col, row)
                self.positions.append(rec)
                for m in moves:
                    if type(m) is list:
                        self.captures[m[1]]=m[0]
                        m=m[1]
                    rec=self.make_rec(m[0], m[1])
                    self.positions.append(rec)

            elif (col+row)%2==1 and self.make_rec(col, row) in self.positions: #clicked selected place
                piece_rec=self.positions[0]
                old_col = self.pos_to_idx(piece_rec.x)
                old_row = self.pos_to_idx(piece_rec.y)

                if (col, row) in self.captures:
                    captured=self.captures[(col, row)]
                    self.board.board[captured[0]][captured[1]]=0

                self.board.move_piece(self.board.board[old_col][old_row].image, col, row, old_col, old_row)
                self.positions=[]
                self.captures={}
            else: #clicked unreachable place
                self.positions=[]
                self.captures={}


    def make_rec(self, col, row):
        return pygame.Rect(self.pos_fix + col*config.piece_size, 
                           self.pos_fix + row*config.piece_size, 
                           config.piece_size, config.piece_size)
    def pos_to_idx(self, pos):
        return int((pos-self.pos_fix)//self.pos_fix)

    def get_con(self):
        assets = AssetManager()
        assets.load_image("king-red")
        return assets.get_image("king-red")
    