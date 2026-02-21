import pygame
import config
from asset import AssetManager
from piece import Piece

class Board():
    def __init__(self):
        self.pos_fix=config.border+config.margin
        self.border_size=config.piece_size*config.board_size+config.border*2

        assets = AssetManager()
        assets.load_pieces()

        self.checker_size=config.piece_size-2*config.piece_fix
        self.color1=assets.get_image("red", self.checker_size)
        self.color2=assets.get_image("black", self.checker_size)
        self.king_color1=assets.get_image("king-red", self.checker_size)
        self.king_color2=assets.get_image("king-black", self.checker_size)
        
        self.board = [
            [0 for _ in range(config.board_size)]
            for _ in range(config.board_size)
        ]
    
    def set_game(self, player):
        if(player=="red"):
            self.color1, self.color2 = self.color2, self.color1
        
        for i in range(config.board_size):
            for j in range(config.board_size):
                if (i+j)%2==1:
                    if i<3:
                        self.board[j][i]=(Piece(self.color1,  j, i, 0))
                    elif i>=5:
                        self.board[j][i]=(Piece(self.color2, j, i, 1))

        
    def draw_board(self, screen):
        rec=pygame.Rect(config.margin, config.margin, self.border_size, self.border_size)
        pygame.draw.rect(screen, config.border_color, rec)
        
        for i in range(config.board_size):
            for j in range(config.board_size):
                color = config.white_color if (i+j)%2==0 else config.black_color
                rec=pygame.Rect(self.pos_fix + i*config.piece_size, self.pos_fix + j*config.piece_size, config.piece_size, config.piece_size)
                pygame.draw.rect(screen, color, rec)

    def draw_pieces(self, screen):
        for row in self.board:
            for piece in row:
                if piece!=0:
                    piece.draw(screen)  


    def valid_moves(self, col, row):
        piece=self.board[col][row]
        player=piece.player
        king=piece.king
        direction= -1 if player==1 else 1
        moves=[]
        for dc,dr in config.directions:
            new_col=col+dc
            new_row=row+dr
            if 0<=new_col<config.board_size and 0<=new_row<config.board_size:
                if self.board[new_col][new_row]==0:
                    if dr==direction or king: # normal forward moves
                        moves.append((new_col,new_row)) 
                else:
                    capture_moves=self.check_capture(new_col, new_row, dc, dr, player)
                    if capture_moves:
                        moves.append(capture_moves)
        return moves

    def check_capture(self, new_col, new_row, dc, dr, player):
        if self.board[new_col][new_row].player!=player: #if enemy
            jump_col=new_col+dc
            jump_row=new_row+dr
            if 0<=jump_col<config.board_size and 0<=jump_row<config.board_size and self.board[jump_col][jump_row]==0 : #if can jump over
                captures=[(new_col, new_row),(jump_col, jump_row)]
                return captures
        else:
            return None


    def move_piece(self, color, col, row, old_col=None, old_row=None):
        player = 0 if color == self.color1 else 1
        
        self.board[old_col][old_row], self.board[col][row] = self.board[col][row], self.board[old_col][old_row]
        self.board[col][row].update(col,row)
        
        if (player == 0 and row == config.board_size-1):
            self.board[col][row].become_king(self.king_color2)
        elif (player == 1 and row == 0):
            self.board[col][row].become_king(self.king_color1)
