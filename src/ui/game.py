import config.config as config
from logic.board import Board
from .renderer import Renderer
from .button import Button

class Game():
    def __init__(self):     
        self.player = config.player
        self.board = Board()
        self.board.set_game(self.player)

        self.renderer = Renderer()
        self.menu_on = False
        self.player_button = Button(text = "Change Player", callback = self.change_player)
        self.bot_button = Button(text = "VS Bot", callback = self.change_to_bot)

        self.selected_moves=[]
        self.selected_piece=None
        self.captures={}


    def draw(self, screen):
        screen.fill((config.back_color))
        
        if self.menu_on:
            self.renderer.draw_menu(screen, self.player_button, self.player, self.bot_button)
            return 
            
        self.renderer.draw_board(screen)
        self.renderer.draw_selected(screen, self.selected_piece, self.selected_moves)
        self.renderer.draw_pieces(screen, self.board.board)
        self.renderer.draw_title(screen, self.board.turn)

    def change_to_bot(self):
        self.board.vs_bot = not self.board.vs_bot
        if self.board.vs_bot:
            print("you are playing against bot now, AI is the future!")
        else:
            print("you are NOT playing against bot now... anyway AI is the future!")
        

    def change_player(self):
        self.player = 1 - self.player
        self.board.set_game(self.player)
        self.board.scan_board_moves()
        self.unselect_pieces()

    def get_icon(self):
        return self.renderer.get_icon()
    
    def handle_click(self, pos):
        if self.menu_on:
            self.player_button.handle_event(pos)
            self.bot_button.handle_event(pos)
            return
        
        col, row = pos
        col=self.pos_to_idx(col)
        row=self.pos_to_idx(row)
        if self.board.in_bounds((col,row)):
            self.click_board(col,row)
    
    def click_board(self, col, row):
        self.selected_piece = self.board.board[col][row]
            
        if self.selected_piece != 0: #selecting a piece
            if self.selected_piece.color == config.players[self.board.turn]: #if correct turn
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
            winner=self.board.turn
            self.board.set_game(winner)
            self.board.is_game_over=False

    def handle_pause(self):
        self.menu_on = not self.menu_on


    def pos_to_idx(self, pos):
        return int((pos-config.pos_fix)//config.piece_size)
