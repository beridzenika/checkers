import pygame
from ui.game import Game
import config.config as config

pygame.init()

screen = pygame.display.set_mode((config.screen_size,config.screen_size))

game = Game()

#display
pygame.display.set_caption("checkers game")
pygame.display.set_icon(game.get_icon())

# time management
clock = pygame.time.Clock()
running = True

while(running):

    #draw
    game.draw(screen)

    game.game_over()

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.handle_click(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.handle_pause()

    pygame.display.flip()   
    clock.tick(60)
pygame.quit()




