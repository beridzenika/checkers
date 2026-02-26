import pygame
import config.config as config
from logic.board import Board
from logic.piece import Piece
from .renderer import Renderer

class Game():
    def __init__(self):     
        self.board = Board()
        self.board.set_game(config.player)

        self.renderer = Renderer()
        
        self.selected_moves=[]
        self.selected_piece=None
        self.captures={}

    def draw(self, screen):
        screen.fill((config.back_color))
        self.renderer.draw_board(screen)
        self.renderer.draw_selected(screen, self.selected_piece, self.selected_moves)
        self.renderer.draw_pieces(screen, self.board.board)
        self.renderer.draw_title(screen, self.board.turn)
    
    def handle_click(self, pos):
        col, row = pos
        col=self.pos_to_idx(col)
        row=self.pos_to_idx(row)
    
        if self.board.in_bounds((col,row)):
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
    
    def game_over(self):
        if self.board.is_game_over:
            winner=config.players[self.board.turn]
            self.board.set_game(winner)
            self.board.is_game_over=False

    
    def pos_to_idx(self, pos):
        return int((pos-config.pos_fix)//config.piece_size)

    def get_icon(self):
        return self.renderer.get_icon()
    