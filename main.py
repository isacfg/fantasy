import pygame, sys

# Iniciando fontes
# pygame.font.init()

# Importing classes
from settings import Settings
from level import Level


if __name__ == '__main__':
    pygame.init() # initializing pygame
    settings = Settings()
    pygame.display.set_caption(settings.game_name) # setando o nome do jogo
    clock = pygame.time.Clock() # criando um relógio para controlar o FPS

    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # criando a tela
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height)) # criando a tela do jogo

    # level 
    level = Level(settings.test_level_map, screen)



    while True:

        for event in pygame.event.get(): # watching for events
            if event.type == pygame.QUIT: # if the user clicked the close button
                pygame.quit() # close the window
                sys.exit() # close the program

        screen.fill(settings.bg_color) # filling the screen with a color

        level.run()

        pygame.display.update() # updating the screen
        clock.tick(settings.FPS) # setting the FPS to 60
        # print(clock.get_fps()) # printing the FPS
        # if clock.get_fps() < 58:
        #     print(f"FPS is too low! {clock.get_fps()}")         