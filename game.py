import pygame
import config
from asset import AssetManager
from board import Board
from piece import Piece

class Game():
    def __init__(self):
        self.assets = AssetManager()
        self.assets.load_pieces(config.piece_size-2*config.piece_fix)
        self.textures=self.assets.textures
        Piece.set_textures(self.textures)

        self.board = Board()
        self.board.set_game(config.player)

        self.pos_fix=config.border+config.margin
        self.border_size=config.piece_size*config.board_size+config.border*2
        self.selected_moves=[]
        self.selected_piece=None
        self.captures={}

    def draw_title(self,screen):
        font = pygame.font.SysFont(None, 48)
        color = config.black_color if self.board.turn else config.border_color
        text_surface = font.render(f"{str.capitalize(config.players[self.board.turn])}'s Turn", True, color)
        screen.blit(text_surface, (20,10))

    def draw_board(self, screen):
        border=pygame.Rect(config.margin, config.margin, self.border_size, self.border_size)
        pygame.draw.rect(screen, config.wood_color, border)
        
        
        pygame.draw.polygon(screen, config.border_color, [
            (config.margin+self.border_size, config.margin+self.border_size),
            (config.margin+self.border_size, config.margin),
            (config.margin, config.margin+self.border_size)
        ])
        
        for col in range(config.board_size): #actual tyles
            for row in range(config.board_size):
                color = config.white_color if (col+row)%2==0 else config.black_color
                pygame.draw.rect(screen, color, self.make_tyle(col, row))

    def draw_pieces(self, screen):
        for row in self.board.board:
            for piece in row:
                if piece!=0:
                    piece.draw(screen)  

    def draw_selected(self, screen):
        if self.selected_piece:
            pygame.draw.rect(screen, config.select_color, self.make_tyle(self.selected_piece.col,self.selected_piece.row))
            for move in self.selected_moves:
                pygame.draw.rect(screen, config.select_color, self.make_tyle(move.to_pos[0],move.to_pos[1]))

    def draw(self, screen):
        screen.fill((config.back_color))
        self.draw_board(screen)
        self.draw_selected(screen)
        self.draw_pieces(screen)
        self.draw_title(screen)


    def handle_click(self, pos):
        col, row = pos
        col=self.pos_to_idx(col)
        row=self.pos_to_idx(row)
    
        if (col >= 0 and col < config.board_size and 0 <= row < config.board_size):
            self.selected_piece = self.board.board[col][row]
            
            if self.selected_piece != 0: #selecting a piece according to turn
                if self.selected_piece.color == config.players[self.board.turn]:

                    if self.board.are_captures:
                        if (col, row) in self.board.capture_moves:
                            self.selected_moves = self.board.capture_moves[(col,row)]
                        else:
                            self.selected_moves = []
                    else:
                        self.selected_moves = self.board.valid_moves(col,row)
                else:
                    self.unselect_pieces()

            for move in self.selected_moves:
                    if move.to_pos == (col, row):
                        self.board.apply_move(move)
                        self.unselect_pieces()

    def unselect_pieces(self):
        self.selected_moves=[]
        self.selected_piece=None

    def make_tyle(self, col, row):
        return pygame.Rect(self.pos_fix + col*config.piece_size, 
                           self.pos_fix + row*config.piece_size, 
                           config.piece_size, config.piece_size)
    
    def game_over(self):
        if self.board.is_game_over:
            self.board.set_game(config.player)
            self.board.is_game_over=False


    
    def pos_to_idx(self, pos):
        return int((pos-self.pos_fix)//config.piece_size)

    def get_icon(self):
        return self.assets.get_image(config.icon)
    