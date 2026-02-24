import config
from piece import Piece
from moves import Moves


class Board():
    def __init__(self):
        self.board = [
            [0 for _ in range(config.board_size)]
            for _ in range(config.board_size)
        ]
        self.player1=config.players[0]
        self.player2=config.players[1]
        self.turn=config.turn
        self.are_captures=False


    def set_game(self, player):
        if(player!=config.players[0]):
            self.player1, self.player2 = self.player2, self.player1
        
        for row in range(config.board_size):
            for col in range(config.board_size):
                if (row+col)%2==1:
                    if row < config.rows:
                        self.board[col][row]=(Piece(self.player1, col, row, 0))
                    elif row >= config.board_size - config.rows:
                        self.board[col][row]=(Piece(self.player2, col, row, 1))
        self.scan_board_moves()

    def valid_moves(self, col, row):
        piece=self.board[col][row]
        from_pos=(col,row)
        moves=[]
        for dc,dr in config.directions:
            new_col = col + dc
            new_row = row + dr
            to_pos = (new_col,new_row)
            if not (0 <= new_col < config.board_size and 
                    0 <= new_row < config.board_size):
                continue
            if self.board[new_col][new_row] == 0: # normal moves
                if dr == piece.direction or piece.king: 
                    moves.append(Moves(from_pos, to_pos))
            else: #captures
                capture_moves=self.check_capture(from_pos, to_pos, dc, dr, piece.color)
                if capture_moves:
                    moves.append(capture_moves)
        return moves

    def check_capture(self, from_pos, enemy_pos, dc, dr, color):
        enemy_color = self.board[enemy_pos[0]][enemy_pos[1]]

        if enemy_color.color != color: #if enemy
            to_pos=(enemy_pos[0] + dc, enemy_pos[1] + dr)
            
            if (0 <= to_pos[0] < config.board_size and 
                0 <= to_pos[1] < config.board_size and 
                self.board[to_pos[0]][to_pos[1]] == 0): #if can jump over
                return Moves(from_pos, to_pos, enemy_pos)
        else:
            return None

    def apply_move(self, move):
        from_col, from_row=move.from_pos
        to_col, to_row=move.to_pos

        piece=self.board[from_col][from_row]
        self.board[to_col][to_row]=piece
        self.board[from_col][from_row]=0
        piece.update(to_col,to_row)
        
        if move.captured:
            cap_col,cap_row = move.captured
            self.board[cap_col][cap_row]=0
            
            self.are_captures = False
            moves = self.valid_moves(to_col, to_row)
            if self.get_capture_moves(moves, to_col, to_row):
                return

        self.set_turn()
        self.scan_board_moves()
        
    
    def scan_board_moves(self):
        self.are_captures = False
        self.capture_moves = {}
        
        for row in range(config.board_size):
            for col in range(config.board_size):
                piece = self.board[col][row]
        
                if(piece != 0 and 
                   piece.color == config.players[self.turn]):
                    moves = self.valid_moves(col, row)
                    self.get_capture_moves(moves, col, row)
        
    def set_turn(self):
        self.turn = 1 - self.turn # change turns from 1-0 and 0-1

    def get_capture_moves(self, moves, col, row):
        capture_moves = [m for m in moves if m.captured]
        if capture_moves:
            self.are_captures = True
            self.capture_moves[(col, row)] = capture_moves
            return True
        return False