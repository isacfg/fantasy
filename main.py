import pygame, sys

# Iniciando fontes
pygame.font.init()

# Importing classes
from settings import Settings
from level import Level
from menu import Menu


if __name__ == '__main__':
    pygame.init() # initializing pygame
    settings = Settings()
    pygame.display.set_caption(settings.game_name) # setando o nome do jogo
    clock = pygame.time.Clock() # criando um relógio para controlar o FPS

    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # criando a tela
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height)) # criando a tela do jogo

    # game 
    level = Level(settings.test_level_map, screen)

    menu = Menu(screen)

    while True:

        for event in pygame.event.get(): # watching for events
            if event.type == pygame.QUIT: # if the user clicked the close button
                pygame.quit() # close the window
                sys.exit() # close the program


        if menu.game_state == 0:
            menu.main_menu()
            menu.draw_text(str(round(clock.get_fps(), 2)),'white', settings.screen_width - 50, 50, 14)


        # Game
        if menu.game_state == 1:
            screen.fill(settings.bg_color) # filling the screen with a color
            level.run()
            # faz o fps aparecer na tela
            menu.draw_text(str(round(clock.get_fps(), 2)),'white', settings.screen_width - 50, 50, 14)

        pygame.display.update() # updating the screen
        clock.tick(settings.FPS) # setting the FPS to 60
        # print(clock.get_fps()) # printing the FPS
     

        # if clock.get_fps() < 58:
        #     print(f"FPS is too low! {clock.get_fps()}")         