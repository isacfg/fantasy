import pygame
import os
import sys
import time
import random

# Iniciando fontes
pygame.font.init()

# Importing settings
from settings import user_settings, game_variables 
from ui.drawBG import drawBackground 

def run_game():
    pygame.init() # initializing pygame

    # System Variables
    pygame.display.set_caption(game_variables["game_name"]) # setando o nome do jogo
    clock = pygame.time.Clock() # criando um relógio para controlar o FPS


    run = True
    while run:
        clock.tick(game_variables["FPS"]) # setando o FPS
        drawBackground() # desenhando o fundo

        for event in pygame.event.get(): # watching for events
            if event.type == pygame.QUIT: # if the user clicked the close button
                run = False # stop the game
                pygame.quit() # close the window
                sys.exit() # close the program
                




run_game() # iniciando o jogo