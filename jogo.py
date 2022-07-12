import pygame
from tiles import Tile
from settings import Settings
from player import Player

settings = Settings()
class Jogo:
    def __init__(self, mapa_test, surface):

        # level setup
        self.display_surface = surface
        self.setup_level(mapa_test) # cria o mundo através do layout das configurações
        self.world_shift = -0 # moves the level
        self.current_x = 0

        self.player_on_ground = False


    def get_player_on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def setup_level(self, layout): # layout is a list of lists that represent the level
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        self.is_player_ground_generated = False
        for row_index, row in enumerate(layout): # enumerate gives you the index and the value
            for col_index, cell in enumerate(row):
                x = col_index * settings.tile_size
                y = row_index * settings.tile_size                
            
                if cell == 'X':
                    tile = Tile((x,y), settings.tile_size, 1) # 1 is the type of tile (value will be random) 1-4
                    self.tiles.add(tile)

                if not self.is_player_ground_generated:
                    tile = Tile((500,800), settings.tile_size, 2)
                    self.tiles.add(tile)
                    self.is_player_ground_generated = True
       
        # adds player na tela
        player_sprite = Player((500,0), self.display_surface)
        self.player.add(player_sprite)

    def scroll_x(self): # ilusao de camera, muda velocidade do mundo
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < settings.screen_width / 4 and direction_x < 0: # 4 is one quarter of the screen, chegando ai a camera se mexe e o player fica parado para criar ilusao de camera
            self.world_shift = 8
            player.speed = 0
        
        elif player_x > settings.screen_width - (settings.screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0

        else:
            self.world_shift = 0
            player.speed = 8

    def h_colision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left

                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right


    def v_colision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False

        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def run(self):


        # level tiles
        self.tiles.update(self.world_shift) 
        self.tiles.draw(self.display_surface)
        self.scroll_x()


        # player
        self.player.update()
        self.h_colision()
        self.get_player_on_ground()
        self.v_colision()
        self.player.draw(self.display_surface)