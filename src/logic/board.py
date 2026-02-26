import config.config as config
from .piece import Piece
from .moves import Moves


class Board():
    def __init__(self):

        self.are_captures = False
        self.is_game_over = False


    def set_game(self, player):
        self.board = [
            [0 for _ in range(config.board_size)]
            for _ in range(config.board_size)
        ]
        self.player1, self.player2 = config.players
        if(player == config.players[0]):
            self.player1, self.player2 = self.player2, self.player1
        
        for row in range(config.board_size):
            for col in range(config.board_size):
                if (row+col)%2==1:
                    if row < config.rows:
                        self.board[col][row]=(Piece(self.player1, col, row, 0))
                    elif row >= config.board_size - config.rows:
                        self.board[col][row]=(Piece(self.player2, col, row, 1))
        self.turn=config.turn
        self.scan_board_moves()

    def valid_moves(self, col, row):
        piece=self.board[col][row]
        moves=[]
        for dirs in config.directions:
            self.move_calculator(piece, moves, self.add_dir((col,row), dirs), dirs)
            
        return moves

    def move_calculator(self, piece, moves, to_pos, dirs):
        from_pos = (piece.col, piece.row)
        if not self.in_bounds(to_pos):
            return
        if self.board[to_pos[0]][to_pos[1]] == 0: # normal moves
            if dirs[1] == piece.direction or piece.king: 
                moves.append(Moves(from_pos, to_pos))
            
            if piece.king:
                self.move_calculator(piece, moves, self.add_dir(to_pos, dirs), dirs)

        elif self.board[to_pos[0]][to_pos[1]].color != piece.color: #captures
            capture_moves = []
            self.check_capture(piece, to_pos, self.add_dir(to_pos, dirs), dirs, capture_moves)
            if capture_moves:
                moves.extend(capture_moves)
            

    def check_capture(self, piece, enemy_pos, to_pos, dirs, capture_moves):
        from_pos=(piece.col, piece.row)
        if not (self.in_bounds(to_pos) and 
            self.board[to_pos[0]][to_pos[1]] == 0): #if can jump over
            return

        capture_moves.append(Moves(from_pos, to_pos, enemy_pos))
        
        if piece.king:
            self.check_capture(piece, enemy_pos, self.add_dir(to_pos, dirs), dirs, capture_moves)


    def apply_move(self, move):
        from_col, from_row=move.from_pos
        to_col, to_row=move.to_pos

        piece=self.board[from_col][from_row]
        self.board[to_col][to_row]=piece
        self.board[from_col][from_row]=0
        piece.update(to_col,to_row)
        
        if move.captured:
            cap_col, cap_row = move.captured
            self.board[cap_col][cap_row] = 0
            
            self.are_captures = False
            moves = self.valid_moves(to_col, to_row)
            if self.get_capture_moves(moves, to_col, to_row):
                return

        self.set_turn()
        self.scan_board_moves()


    def scan_board_moves(self):
        self.are_captures = False
        self.capture_moves = {}
        has_piece = False
        has_move = False

        for row in range(config.board_size):
            for col in range(config.board_size):
                piece = self.board[col][row]

                if piece and piece.color == config.players[self.turn]:
                    has_piece = True
                    moves = self.valid_moves(col, row)
                    if moves:
                        has_move = True
                        self.get_capture_moves(moves, col, row)
                        
        if not has_piece or not has_move:
            self.is_game_over = True
            self.set_turn()

    def get_capture_moves(self, moves, col, row): 
        capture_moves = [m for m in moves if m.captured] 
        if capture_moves: 
            self.are_captures = True 
            self.capture_moves[(col, row)] = capture_moves 
            return True 
        return False


    def set_turn(self):
        self.turn = 1 - self.turn # change turns from 1-0 and 0-1

    @staticmethod
    def in_bounds(pos):
        return 0 <= pos[0] < config.board_size and 0 <= pos[1] < config.board_size
    
    @staticmethod
    def add_dir(pos, dirs):
        return (pos[0] + dirs[0], pos[1] + dirs[1])
