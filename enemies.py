import pygame, random
from importer import import_folder
from global_variables import *

from settings import Settings

settings = Settings()

class Enemies(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.import_enemy_sprites()
        self.display_surface = surface

        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        self.facing_right = False
        self.on_ground = False
        self.on_ceiling = False

        # physics
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3
        self.gravity = 0.8


    def import_enemy_sprites(self):
        character_path = './assets/enemies/'
        self.animations = {
            'idle': [],
            'run': [],
            'attack_1': [],
            'death': [],
        }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path, True) # true resizes to setings player width and height
                
    def get_status(self):
        # self.status = 'idle'
        if self.direction.x == 0:
            self.status = 'idle'

        elif self.direction.x == -1:
            self.facing_right = False
            self.status = 'run'

        elif self.direction.x == 1:
            self.facing_right = True
            self.status = 'run'

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_j]:
            self.direction.x = -1
            self.facing_right = False

        elif keys[pygame.K_l]:
            self.direction.x = 1
            self.facing_right = True

   
    def animate(self):
        enemy_animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(enemy_animation):
            self.frame_index = 0

        enemy_image = enemy_animation[int(self.frame_index)]
        if not self.facing_right:
            flipped_enemy_image = pygame.transform.flip(enemy_image, True, False)
            self.image = flipped_enemy_image
        else:
            self.image = enemy_image

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        # print(f"gravity was called")

    def draw(self):
        self.display_surface.blit(self.image, self.rect)

    def get_enemy_position(self):
        return self.rect.x, self.rect.y

    def kill_enemy(self):
        if self.rect.y > settings.screen_height:
            return True

    def random_movement(self):

        self.direction.x = random.randint(-1, 1)
        self.direction.y = random.randint(-1, 1)

        pass

    def update(self):
        self.get_status()
        self.get_input()
        self.animate()