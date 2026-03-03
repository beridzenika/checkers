import pygame

class Button:
    def __init__(self, text, callback):
        self.callback = callback  # function to call when clicked
        self.text = text
        self.rect = None
        self.font = pygame.font.SysFont(None, 32)

    def draw(self, screen, color, pos, text_color):
        text_surface = self.font.render(self.text, True, text_color)

        width, height = text_surface.get_size()
        self.rect = pygame.Rect(pos[0], pos[1], width+20, height+10)
        pygame.draw.rect(screen, color, self.rect)
        
        screen.blit(text_surface, text_surface.get_rect(center=self.rect.center))

    def handle_event(self, pos):
        if self.rect and self.rect.collidepoint(pos):
            self.callback()