import pygame, sys
import os

# Iniciando fontes
# pygame.font.init()

# Importing classes
from settings import Settings
from player import Player    

class Game:
    def __init__(self):
        self.run = True
        self.player_sprite = Player()
        self.player_sprite_group = pygame.sprite.Group()
        self.player_sprite_group.add(self.player_sprite)

    
    
    def run_game(self):
        # all the code for the game

        self.player_sprite.update()
        self.player_sprite_group.draw(screen) # drawing the player on the screen

        


if __name__ == '__main__':
    settings = Settings()    

    pygame.init() # initializing pygame
    pygame.display.set_caption(settings.game_name) # setando o nome do jogo
    clock = pygame.time.Clock() # criando um relógio para controlar o FPS

    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # criando a tela
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height)) # criando a tela do jogo
    game = Game() # iniciando a classe Game


    # temporary code


    while game.run:
        for event in pygame.event.get(): # watching for events
            if event.type == pygame.QUIT: # if the user clicked the close button
                game.run = False # stop the game
                pygame.quit() # close the window
                sys.exit() # close the program

        screen.fill(settings.bg_color) # filling the screen with a color

        game.run_game() # running the game

        pygame.display.update() # updating the screen
        clock.tick(settings.FPS) # setting the FPS to 60
                    