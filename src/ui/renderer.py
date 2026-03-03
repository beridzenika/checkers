import pygame
import config.config as config
from assets.asset import AssetManager 


class Renderer:
    def __init__(self):
        self.assets = AssetManager()
        self.assets.load_pieces(config.piece_size-2*config.piece_fix)
        self.textures=self.assets.textures

        self.border_size=config.piece_size*config.board_size+config.border*2
        self.piece_pos_fix = config.pos_fix + config.piece_fix

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


    def draw_selected(self, screen, selected_piece, selected_moves):
        if selected_piece:
            pygame.draw.rect(screen, config.select_color, self.make_tyle(selected_piece.col, selected_piece.row))
            for move in selected_moves:
                pygame.draw.rect(screen, config.select_color, self.make_tyle(move.to_pos[0],move.to_pos[1]))


    def draw_pieces(self, screen, board):
        for row in board:
            for piece in row:
                if piece!=0:
                    texture = self.textures[f"king-{piece.color}" if piece.king else piece.color]
                    rec = texture.get_rect(topleft=(self.piece_pos_fix + piece.col * config.piece_size, 
                                               self.piece_pos_fix + piece.row * config.piece_size))
                    screen.blit(texture, rec)


    def draw_title(self,screen, turn):
        font = pygame.font.SysFont(None, 48)
        color = config.black_color if turn else config.border_color
        text_surface = font.render(f"{str.capitalize(config.players[turn])}'s Turn", True, color)
        screen.blit(text_surface, (20,10))


    def draw_menu(self, screen, player_button, player, bot_button):
        x=config.margin
        y=config.margin*2
        w=self.border_size
        h=self.border_size/3*2
        marg=20
        pad=50
        pygame.draw.rect(screen, config.wood_color, (x, y, w, h))
        pygame.draw.rect(screen, config.white_color, (x+marg, y+marg, w-marg*2, h-marg*2))

        font = pygame.font.SysFont(None, 32)

        text_surface = font.render(f"Player1 {str.capitalize(config.players[player])}", True, config.border_color)
        screen.blit(text_surface, (x+pad,y+pad))

        text_surface = font.render(f"Player2 {str.capitalize(config.players[1 - player])}", True, config.border_color)
        screen.blit(text_surface, (w/2+x+pad,y+pad))

        player_button.draw(screen, config.border_color, (x+pad, y+pad*2), config.white_color)

        bot_button.draw(screen, config.border_color, (w/2+x+pad, y+pad*2), config.white_color)
        



    def get_icon(self):
        return self.assets.get_image(config.icon)


    def make_tyle(self, col, row):
        return pygame.Rect(config.pos_fix + col*config.piece_size, 
                           config.pos_fix + row*config.piece_size, 
                           config.piece_size, config.piece_size)
