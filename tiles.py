import pygame
from random import randint
from settings import Settings
from importer import import_folder
settings = Settings()

# Todo
# Adicionar sprites for tiles

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, random_value):
        super().__init__()
        self.selected_tile = 1
        
        # self.selected_tile = randint(1,5) # random tile
        self.selected_tile = random_value

        if self.selected_tile == 1:
            self.image = pygame.image.load('./assets/tiles/tile01.png').convert_alpha()
        elif self.selected_tile == 2:
            self.image = pygame.image.load('./assets/tiles/tile02.png').convert_alpha()
        elif self.selected_tile == 3:
            self.image = pygame.image.load('./assets/tiles/tile03.png').convert_alpha()
        elif self.selected_tile == 4:
            self.image = pygame.image.load('./assets/tiles/tile04.png').convert_alpha()

        # self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)

        # self.images = []

    # def import_tiles(self):
    #     tile_path = './assets/tiles'
    #     tile_list = []

    def update(self,x_shift): # x_shift é o deslocamento da tela
        self.rect.x += x_shift