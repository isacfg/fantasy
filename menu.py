import pygame

from settings import Settings

settings = Settings()

# todo
# change font 

class Menu():
    def __init__(self, window):
        self.screen = window
        self.font_name = './assets/fonts/PressStart2P-Regular.ttf'
        self.font_size_big = 30
        self.font_size_medium = 18

        self.game_state = 0 # 0 is the menu screen
        self.selected_option = 0

        # positions
        self.screen_center = settings.screen_width / 2
        self.title_y = 125
        self.text_y_offset = 50
        self.text_y_1 = 300
        self.text_y_2 = self.text_y_1 + self.text_y_offset
        self.text_y_3 = self.text_y_2 + self.text_y_offset

        self.arrow_image = pygame.image.load('assets/arrow.png')
        self.arrow_image = pygame.transform.scale(self.arrow_image, (18.6667 * 1.5, 21.33334 * 1.5))
        self.arrow_image_rect =  self.arrow_image.get_rect(center = (500, 300))

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_m]: # press m to play
            self.game_state = 1

        if keys[pygame.K_DOWN]:
            self.arrow_image_rect.y = self.text_y_2

    def draw_text(self,text,color,x,y, font_size):
        self.font = pygame.font.Font(self.font_name, font_size) # fontname, size

        self.text_obj = self.font.render(text, 1, color)
        self.text_rect = self.text_obj.get_rect()
        self.text_rect.center = (x,y)
        self.screen.blit(self.text_obj, self.text_rect)

    def main_menu(self):
        self.screen.fill((32, 32, 32))
        self.get_input()

        # Texts
        self.draw_text('MAIN MENU', 'white', self.screen_center , 125, self.font_size_big) #text, color, x,y, font size
        self.draw_text('PLAY', 'white', self.screen_center, self.text_y_1 , self.font_size_medium)
        self.draw_text('CONTROLS', 'white', self.screen_center, self.text_y_2, self.font_size_medium)
        self.draw_text('CREDITS', 'white', self.screen_center, self.text_y_3, self.font_size_medium)

        # temporary
        # self.mx, self.my = pygame.mouse.get_pos()
        # self.draw_text('*','white', self.mx, self.my, 25)
        # self.button_1 = pygame.Rect(50,100,200,50)
        # pygame.draw.rect(self.screen, (255,0,0), self.button_1)


        self.screen.blit(self.arrow_image, (self.arrow_image_rect.x, self.arrow_image_rect.y))            