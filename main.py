import pygame
import config
from asset import AssetManager
from checkers import Checkers
from board import Board

pygame.init()

screen = pygame.display.set_mode((config.screen_size,config.screen_size))

# get images
assets = AssetManager()
king_red=assets.get_image("king-red")

#board
board = Board()

#pieces
pieces=Checkers()
pieces.set_game(config.player)

#display
pygame.display.set_caption("checkers game")
pygame.display.set_icon(king_red)

# time management
clock = pygame.time.Clock()
running = True

while(running):
    screen.fill((config.back_color))

    #draw
    board.draw(screen)
    pieces.draw(screen)

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)
pygame.quit()