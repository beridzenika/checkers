import pygame
from game import Game
import config

pygame.init()

screen = pygame.display.set_mode((config.screen_size,config.screen_size))

game = Game()

#display
pygame.display.set_caption("checkers game")
pygame.display.set_icon(game.get_con())

# time management
clock = pygame.time.Clock()
running = True

while(running):

    #draw
    game.draw(screen)

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.handle_click(pygame.mouse.get_pos())


    pygame.display.flip()
    clock.tick(60)
pygame.quit()