import pygame
from global_variables import *
from settings import Settings

settings = Settings()

class Controls:
    def __init__(self, window):
        self.screen = window

        # background
        self.background = pygame.image.load('assets/bg_controls.png')
        self.background_rect = self.background.get_rect(topleft = (0,-0))

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]: # voltar menu
            set_game_state(0)

    def draw_main_text(self):
        draw_text('CONTROLS', 'white', settings.screen_width / 2, 125, 30, self.screen) # text, color , x, y, font size, screen


    def run(self):
        self.screen.fill(settings.bg_color)
        self.screen.blit(self.background, (self.background_rect.x, self.background_rect.y))
        self.draw_main_text()

        self.get_input()