import pygame
from pygame import mixer
from tiles import Tile
from settings import Settings
from player import Player
from global_variables import *

from enemies import Enemies

class Jogo:
    def __init__(self, mapa_test, surface):
        self.settings = Settings()

        # level setup
        self.display_surface = surface
        self.setup_level(mapa_test) # cria o mundo através do layout das configurações
        # self.first_enemy()
        self.world_shift = -0 # moves the level
        self.current_x = 0

        self.player_on_ground = False

        self.enemies = []
        self.generate_enemies(2, True) # quantidade, first enemy true 
        self.limit_generated_enemies = 0
        self.stop_generating_enemies = False
        self.player_x_position = 0
        self.player_y_position = 0


    def get_player_on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def setup_level(self, layout): # layout is a list of lists that represent the level
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout): # enumerate gives you the index and the value


            for col_index, cell in enumerate(row):
                x = col_index * self.settings.tile_size
                y = row_index * self.settings.tile_size                
            
                if cell == 'X':
                    tile = Tile((x,y), self.settings.tile_size, 'X') 
                    self.tiles.add(tile)
                elif cell == 'F':
                    tile = Tile((x,y), self.settings.tile_size, 'F') 
                    self.tiles.add(tile)
                elif cell == 'G':
                    tile = Tile((x,y), self.settings.tile_size, 'G') 
                    self.tiles.add(tile)
                elif cell == 'I':
                    tile = Tile((x,y), self.settings.tile_size, 'I') 
                    self.tiles.add(tile)
               
       
        # adds player na tela

        player_tile = Tile((600,500), self.settings.tile_size, 'X')
        self.tiles.add(player_tile)

        player_sprite = Player((600,0), self.display_surface)
        self.player.add(player_sprite)

    def scroll_x(self): # ilusao de camera, muda velocidade do mundo
        player = self.player.sprite
        player_x = player.rect.centerx
        self.player_x_position = player_x
        self.player_y_position = player.rect.centery
        direction_x = player.direction.x

        # enemy = self.enemy.sprites()
        # enemy_x = enemy.rect.centerx

        
        if player_x < self.settings.screen_width / 4 and direction_x < 0: # 4 is one quarter of the screen, chegando ai a camera se mexe e o player fica parado para criar ilusao de camera
            self.world_shift = 8
            player.speed = 0
            # # for enemy in self.enemy.sprites():
                # enemy.direction.x = 1
                # enemy.speed = 8

            for enemy in self.enemies:
                enemy.direction.x = 1
                enemy.speed = 8
         
        
        elif player_x > self.settings.screen_width - (self.settings.screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
            # # for enemy in self.enemy.sprites():
                # enemy.direction.x = -1
                # enemy.speed = 8

            for enemy in self.enemies:
                enemy.direction.x = -1
                enemy.speed = 8

        else:
            self.world_shift = 0
            player.speed = 8
            # # for enemy in self.enemy.sprites():
                # enemy.speed = 8
                # enemy.direction.x = 0
            
            for enemy in self.enemies:
                enemy.speed = 8
                # enemy.direction.x = 0

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

    def enemy_h_colision(self):
        # enemy = self.enemy.sprites
        # enemy.rect.x += enemy.direction.x * enemy.speed
        # # for enemy in self.enemy.sprites():
            # # # enemy.rect.x += enemy.direction.x * enemy.speed

        for enemy in self.enemies:
            enemy.rect.x += enemy.direction.x * enemy.speed

            keys = pygame.key.get_pressed()
            if keys[pygame.K_j]:
                enemy.direction.x = -1

        # horizontal colision
        for enemy in self.enemies:
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(enemy.rect):
                    if enemy.direction.x < 0:
                        enemy.rect.left = sprite.rect.right
                        enemy.on_left = True
                        enemy.direction.x = 1
                    elif enemy.direction.x > 0:
                        enemy.rect.right = sprite.rect.left
                        enemy.on_right = True
                        enemy.direction.x = -1

    def enemy_v_colision(self):
     
        for enemy in self.enemies:
            enemy.apply_gravity()
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(enemy.rect):
                    if enemy.direction.y < 0:
                        enemy.rect.top = sprite.rect.bottom
                        enemy.direction.y = 0
                        enemy.on_ceiling = True
                    elif enemy.direction.y > 0:
                        enemy.rect.bottom = sprite.rect.top
                        enemy.direction.y = 0
                        enemy.on_ground = True

                # if sprite.rect.colliderect((enemy.rect.x + 1 + enemy.rect.width, enemy.rect.y + enemy.rect.height + 1, enemy.rect.width, enemy.rect.height)):
                #     enemy.direction.x = +1
                #     # print('going right')
                # elif sprite.rect.colliderect((enemy.rect.x + 1 - enemy.rect.width, enemy.rect.y + enemy.rect.height + 1, enemy.rect.width, enemy.rect.height)):
                #     enemy.direction.x = -1
                #     # print('going left')
                
                    

    
    def generate_enemies(self, i = 1, First_enemy = False, Automatic = False):
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_v]:

        #     self.enemy = pygame.sprite.GroupSingle()
        #     enemy_sprite = Enemies((500,0), self.display_surface)
            # self.enemy.add(enemy_sprite)s
        if get_time() > 1:
            if Automatic and int(self.limit_generated_enemies) > 1 and self.stop_generating_enemies == False:
                random_x_1 = get_random_int(30, self.settings.screen_width - 30)
                random_x_2 = get_random_int(30, self.settings.screen_width - 30)
                random_x_3 = get_random_int(30, self.settings.screen_width - 30)
                random_x_4 = get_random_int(30, self.settings.screen_width - 30)
                self.enemies.append(Enemies((random_x_1,-20), self.display_surface))
                self.enemies.append(Enemies((random_x_2,-20), self.display_surface))
                self.enemies.append(Enemies((random_x_3,-20), self.display_surface))
                # self.enemies.append(Enemies((random_x_4,-20), self.display_surface))
                print(f"automatic enemy generated")
                self.limit_generated_enemies = 0
            
            else:
                if First_enemy:
                    for j in range(0, i + 1):
                        self.enemies.append(Enemies((500,0), self.display_surface))

                elif not First_enemy and int(self.limit_generated_enemies) > 1:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_v]:
                        self.enemies.append(Enemies(( get_random_int(30, self.settings.screen_width - 30),0), self.display_surface))
                        print(f"manual enemy generated")
                        self.limit_generated_enemies = 0


    def toggle_enemies_generation(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_n]:
            self.stop_generating_enemies = False

        if keys[pygame.K_b]:
            self.stop_generating_enemies = True
            self.enemies = []
            print(f"stop generating enemies")

    def check_enemies_colision(self):

        for enemy in self.enemies:

            if self.player.sprite.rect.colliderect(enemy.rect):
                self.enemies = []
                death_sfx = mixer.Sound('./assets/music/hit.mp3')
                death_sfx.set_volume(0.2)
                death_sfx.play()                
                set_game_state(9)
  
                    
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

        # enemy
        # self.enemy.update()
        # self.enemy_h_colision()
        # self.enemy_v_colision()
        # self.generate_enemies()
        # # for enemy in self.enemy.sprites():
            # self.enemy.draw(self.display_surface)

        # self.enemy.draw(self.display_surface)
        self.enemy_v_colision()
        self.generate_enemies() # manual enemy generation (press v)
        self.limit_generated_enemies += 0.2
        self.toggle_enemies_generation()
        self.check_enemies_colision()

        if get_time() % 2 == 0:
            self.generate_enemies(1, False, True)
            for k, enemy in enumerate(self.enemies):
                self.enemies[k].random_movement()
                # print(f"RECT: {self.enemies[k].rect}")
                

        for i in range(0, len(self.enemies)):
            self.enemies[i].update()
            self.enemies[i].draw()
            # print(f"enemy {i} pos {self.enemies[i].get_enemy_position()}")

            # follows player
            # if self.player_x_position > self.enemies[i].rect.x:
            #     self.enemies[i].direction.x = 1
            # elif self.player_x_position < self.enemies[i].rect.x:
            #     self.enemies[i].direction.x = -1

        for k, enemy in enumerate(self.enemies):

            if self.enemies[k].kill_enemy():
                del self.enemies[k]
                print(f"enemy {k} killed")    

        self.enemy_h_colision()
            

