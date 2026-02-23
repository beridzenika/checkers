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

    def set_game(self, player):
        if(player!=config.players[0]):
            self.player1, self.player2 = self.player2, self.player1
        
        for i in range(config.board_size):
            for j in range(config.board_size):
                if (i+j)%2==1:
                    if i < config.rows:
                        self.board[j][i]=(Piece(self.player1, j, i, 0))
                    elif i >= config.board_size - config.rows:
                        self.board[j][i]=(Piece(self.player2, j, i, 1))

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
            if self.board[new_col][new_row]==0:
                if dr==piece.direction or piece.king: # normal forward moves
                    moves.append(Moves(from_pos, to_pos))
            else:
                capture_moves=self.check_capture(from_pos, to_pos, dc, dr, piece.color)
                if capture_moves:
                    moves.append(capture_moves)
        return moves

    def check_capture(self, from_pos, to_pos, dc, dr, color):
        if self.board[to_pos[0]][to_pos[1]].color!=color: #if enemy
            captured=to_pos
            to_pos=(to_pos[0]+dc, to_pos[1]+dr)
            if 0<=to_pos[0]<config.board_size and 0<=to_pos[1]<config.board_size and self.board[to_pos[0]][to_pos[1]]==0 : #if can jump over
                return Moves(from_pos, to_pos, captured)
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


