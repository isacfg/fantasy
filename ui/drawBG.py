import pygame
import os
import time
import random


from settings import user_settings, game_variables 

screen = pygame.display.set_mode( (user_settings["screen_width"], user_settings["screen_height"]) )

background = pygame.image.load(os.path.join("assets", "sunsetCity.png")) # carregando a imagem de fundo
background = pygame.transform.scale(background, (user_settings["screen_width"], user_settings["screen_height"])) # redimensionando a imagem de fundo


def drawBackground():
    screen.blit(background, (0, 0))