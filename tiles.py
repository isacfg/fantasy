import pygame
from random import randint
from settings import Settings
from importer import import_folder
settings = Settings()

# Todo
# Adicionar sprites for tiles

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, selected_tile):
        super().__init__()
        self.selected_tile = selected_tile
        if self.selected_tile == 'X':
            self.image = pygame.image.load('./assets/tiles/tile01.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (size, size))
            self.rect = self.image.get_rect(topleft = pos)
        elif self.selected_tile == 'F':
            self.image = pygame.image.load('./assets/tiles/tile02.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (size, size))
            self.rect = self.image.get_rect(topleft = pos)
        elif self.selected_tile == 'G':
            self.image = pygame.image.load('./assets/tiles/tile03.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (size, size))
            self.rect = self.image.get_rect(topleft = pos)
        elif self.selected_tile == 'I':
            self.image = pygame.image.load('./assets/tiles/tile04.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (size, size))
            self.rect = self.image.get_rect(topleft = pos)

        # self.images = []

    # def import_tiles(self):
    #     tile_path = './assets/tiles'
    #     tile_list = []

    def update(self,x_shift): # x_shift é o deslocamento da tela
        self.rect.x += x_shift