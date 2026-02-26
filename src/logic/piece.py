import config.config as config

class Piece:
    def __init__(self, color, col, row, player):
        self.color = color
        self.col = col
        self.row = row
        self.direction = -1 if player==1 else 1
        self.promotion_row = 0 if player==1 else config.board_size-1
        self.king=False
        self.update(self.col, self.row)    
    
    def become_king(self):
        self.king = True
    
    def update(self, col,row):
        self.col = col
        self.row = row
        if self.promotion_row == row:
            self.become_king()
