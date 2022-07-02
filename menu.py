import pygame
from settings import Settings
# from main import game_state_global

from global_variables import get_game_state, set_game_state


settings = Settings()



class Menu():
    def __init__(self, window):
        self.screen = window
        self.font_name = './assets/fonts/PressStart2P-Regular.ttf'
        self.font_size_big = 30
        self.font_size_medium = 18

		# background
        self.background_shift = 8
        self.shift_acumulator = 0
        self.limit_user_input = 0

        self.background = pygame.image.load('assets/bg.png')
        self.background = pygame.transform.scale(self.background, (settings.screen_width, settings.screen_height))
        self.background_rect = self.background.get_rect(topleft = (0,-0))


        # self.game_state = 0 # 0 is the menu screen
        self.selected_option = 1 # 1 is the play option

        # positions
        self.screen_center = settings.screen_width / 2
        self.title_y = 125
        self.text_y_offset = 75
        self.text_y_1 = 300
        self.text_y_2 = self.text_y_1 + self.text_y_offset
        self.text_y_3 = self.text_y_2 + self.text_y_offset
        self.text_y_4 = self.text_y_3 + self.text_y_offset

        self.arrow_offset = 0

        self.arrow_image = pygame.image.load('assets/arrow.png')
        self.arrow_image = pygame.transform.scale(self.arrow_image, (18.6667 * 1.5, 21.33334 * 1.5))
        self.arrow_image_rect =  self.arrow_image.get_rect(topleft = (520, 285))


    def get_input(self):
        keys = pygame.key.get_pressed()
        self.limit_user_input += 0.5

        if keys[pygame.K_RETURN] and self.selected_option == 1: # press ENTER to play
            set_game_state(1)

        if keys[pygame.K_RETURN] and self.selected_option == 2: # press ENTER to controls
            pass

        if keys[pygame.K_RETURN] and self.selected_option == 3: # press ENTER to credits
            pass

        if keys[pygame.K_RETURN] and self.selected_option == 4: # press ENTER to quit
            pygame.quit()


        if keys[pygame.K_DOWN] and self.selected_option == 1 and int(self.limit_user_input) > 1:
            self.arrow_image_rect.y = 360 # y of controls
            self.arrow_image_rect.x = 485 # x of controls
            self.selected_option = 2 # 2 is the controls option
            self.limit_user_input = 0
           

        if keys[pygame.K_DOWN] and self.selected_option == 2 and int(self.limit_user_input) > 1:
            self.arrow_image_rect.y = 435 # y of credits
            self.arrow_image_rect.x = 495 # x of credits
            self.selected_option = 3 # 3 is the credits option
            self.limit_user_input = 0


        if keys[pygame.K_DOWN] and self.selected_option == 3 and int(self.limit_user_input) > 1:
            self.arrow_image_rect.y = 510 # y of quit
            self.arrow_image_rect.x = 520  # x of quit
            self.selected_option = 4 # 4 is the quit option
            self.limit_user_input = 0


        if keys[pygame.K_UP] and self.selected_option == 2 and int(self.limit_user_input) > 1:
            self.arrow_image_rect.y = 285 # y of play
            self.arrow_image_rect.x = 520 # x of play
            self.selected_option = 1 # 1 is the play option
            self.limit_user_input = 0


        if keys[pygame.K_UP] and self.selected_option == 3 and int(self.limit_user_input) > 1:
            self.arrow_image_rect.y = 360 # y of controls
            self.arrow_image_rect.x = 485 # x of controls
            self.selected_option = 2 # 2 is the controls option
            self.limit_user_input = 0


        if keys[pygame.K_UP] and self.selected_option == 4 and int(self.limit_user_input) > 1:
            self.arrow_image_rect.y = 435 # y of credits
            self.arrow_image_rect.x = 495 # x of credits
            self.selected_option = 3 # 3 is the credits option
            self.limit_user_input = 0


    def draw_text(self,text,color,x,y, font_size):
        self.font = pygame.font.Font(self.font_name, font_size) # fontname, size

        self.text_obj = self.font.render(text, 1, color)
        self.text_rect = self.text_obj.get_rect()
        self.text_rect.center = (x,y)
        self.screen.blit(self.text_obj, self.text_rect)

    def draw_background(self):
        self.screen.blit(self.background, (self.background_rect.x, self.background_rect.y))
        # self.shift_acumulator = self.shift_acumulator - self.background_shift
        # self.background_rect.x = int(self.shift_acumulator)
        
        # if (self.background_rect.x <= 0 or self.background_rect.x >= -8):
        #     self.backgroundF = pygame.transform.flip(self.background, True, False) # image, flip x, flip y
        #     self.screen.blit(self.backgroundF, (self.background_rect.x + settings.screen_width, self.background_rect.y))


    def main_menu(self):
        self.screen.fill(settings.bg_color)
        self.draw_background()
        self.get_input()

        # Texts
        self.draw_text('MAIN MENU', 'white', self.screen_center , 125, self.font_size_big) #text, color, x,y, font size
        self.draw_text('PLAY', 'white', self.screen_center, self.text_y_1 , self.font_size_medium)
        self.draw_text('CONTROLS', 'white', self.screen_center, self.text_y_2, self.font_size_medium)
        self.draw_text('CREDITS', 'white', self.screen_center, self.text_y_3, self.font_size_medium)
        self.draw_text('QUIT', 'white', self.screen_center, self.text_y_4, self.font_size_medium)

        # temporary
        # self.mx, self.my = pygame.mouse.get_pos()
        # self.draw_text('*','white', self.mx, self.my, 25)
        # self.button_1 = pygame.Rect(50,100,200,50)
        # pygame.draw.rect(self.screen, (255,0,0), self.button_1)


        self.screen.blit(self.arrow_image, (self.arrow_image_rect.x, self.arrow_image_rect.y)) 
        # print(f"BACKGROUND X:{self.background_rect.x}")  
        # print(self.limit_user_input)         