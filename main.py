import pygame, sys
from pygame import mixer

# Iniciando fontes
pygame.font.init()

# Importing classes
from settings import Settings
from jogo import Jogo
from menu import Menu
from controls import Controls
from credits_game import Credits

# temp
from enemies import Enemies

from global_variables import *
from random_map import *



if __name__ == '__main__':
    pygame.init() # initializing pygame
    settings = Settings()
    pygame.display.set_caption(settings.game_name) # setando o nome do jogo
    clock = pygame.time.Clock() # criando um relógio para controlar o FPS
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height)) # criando a tela do jogo

    # game 
    level = Jogo(settings.test_level_map, screen)
    menu = Menu(screen)
    controls = Controls(screen)
    credits_game = Credits(screen)
    print(f"Game state: {get_game_state()}")

    # music
    mixer.music.load('./assets/music/menu.wav')
    # mixer.music.load('./assets/music/bg.wav')
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)

    start_time()
    max_score = 0

    while True:
        # print(get_time())
    
    
        for event in pygame.event.get(): # watching for events
            if event.type == pygame.QUIT: # if the user clicked the close button, fecha o jogo
                pygame.quit() # close the window
                sys.exit() # close the program

        if get_game_state() == 9: # reset
            if get_time() > max_score:
                max_score = get_time()

            reset_map()
            reset_time()
            settings = Settings()
            level = Jogo(settings.test_level_map, screen)
            menu = Menu(screen)
            set_game_state(0)


        if get_game_state() == 0: # global variable diz em qual tela the game is

            menu.run()
            menu.draw_text(str(round(clock.get_fps(), 2)),'white', settings.screen_width - 50, 50, 14)

            menu.draw_text(f"{str(get_time())}", 'white',50, 50, 14)
            menu.draw_text(f"{str(max_score)}", 'white', 50, 100, 14)


        # Game
        if get_game_state() == 1: # play state

            
            screen.fill(settings.bg_color) # filling the screen with a color
            level.run()
            # enemy.update()
            # show fps
            menu.draw_text(str(round(clock.get_fps(), 2)),'white', settings.screen_width - 50, 50, 14)
                
            menu.draw_text(f"{str(get_time())}", 'white',50, 50, 14)
            menu.draw_text(f"{str(max_score)}", 'white', 50, 100, 14)           

        pygame.display.update() # updating the screen

        if get_game_state() == 2: # controls state # add states to menu
            # print("game state 2, controls")

            controls.run()

        if get_game_state() == 3: # credits state
            credits_game.run()

        # FPS
        if get_game_state() == 0: 
            clock.tick(settings.MENU_FPS) # limit the FPS to 30 para consertar bug em que seta passa mais de uma vez por call
        else:
            clock.tick(settings.FPS)
     

         