import pygame
from random import randint
from settings import Settings
from importer import import_folder
settings = Settings()

# Todo
# Adicionar sprites for tiles

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        

        self.image = pygame.image.load('./assets/tiles/tile01.png').convert_alpha()
  

        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)

        # self.images = []

    # def import_tiles(self):
    #     tile_path = './assets/tiles'
    #     tile_list = []

    def update(self,x_shift): # x_shift é o deslocamento da tela
        self.rect.x += x_shift