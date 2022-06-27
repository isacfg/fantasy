import pygame
from tiles import Tile
from settings import Settings
from player import Player

settings = Settings()
class Level:
    def __init__(self, level_data, surface):

        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = -0 # how much the world has move to the left

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * settings.tile_size
                y = row_index * settings.tile_size                
            
                if cell == 'X':
                    tile = Tile((x,y), settings.tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)


    def run(self):
        # level tiles
        self.tiles.update(self.world_shift) 
        self.tiles.draw(self.display_surface)

        # player
        self.player.update()
        self.player.draw(self.display_surface)