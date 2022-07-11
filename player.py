import pygame, os
from settings import Settings
from importer import import_folder

from global_variables import get_game_state, set_game_state


settings = Settings()

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0 # current sprite frame
        self.animation_speed = 0.15 # animation speed
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        
        # particulas de correr
        self.import_dust_run_particles()
        self.dust_frame_index = 0 # current sprite frame
        self.dust_animation_speed = 0.15 # animation speed
        self.display_surface = surface

        # physics
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        # status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False


    def import_character_assets(self):
        character_path = './assets/player/'
        self.animations = {
            'idle': [], 
            'run': [], 
            'jump': [], 
            'fall': [], 
            'take_damage': [], 
            'death': [],
            'dodge': [],
            'attack_1': [],
            'attack_2': [],
            'attack_3': [],
            'attack_4': [],
            }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path, True) # True to scale to seetings player width and height, useful por que particulas nao precisam escalar

    def import_dust_run_particles(self): # run particles
        self.dust_run_particles = import_folder('./assets/player/dust_particles/run')

    def run_dust_animation(self):
        if self.status == 'run' and self.on_ground:
            self.dust_frame_index += self.dust_animation_speed
            if self.dust_frame_index >= len(self.dust_run_particles):
                self.dust_frame_index = 0

            dust_particle = self.dust_run_particles[int(self.dust_frame_index)]

            if self.facing_right:
                pos = self.rect.bottomleft - pygame.math.Vector2(6, 10)
                self.display_surface.blit(dust_particle, pos)

            if self.facing_right == False:
                pos = self.rect.bottomright - pygame.math.Vector2(6, 10)
                flipped_dust_particle = pygame.transform.flip(dust_particle, True, False)
                self.display_surface.blit(flipped_dust_particle, pos)

    def animate(self):
        animation = self.animations[self.status]

        # loop frame index
        self.frame_index += self.animation_speed 
        if self.frame_index >= len(animation):
            self.frame_index = 0 # loop

        image = animation[int(self.frame_index)]
        if self.facing_right == True:
            self.image = image
        else:
            f_image = pygame.transform.flip(image, True, False) # image, flip x, flip y
            self.image = f_image


    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            set_game_state(0) # menu

        if keys[pygame.K_a]:
            self.direction.x = -1
            self.facing_right = False

        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.facing_right = True

        else:
            self.direction.x = 0

        if keys[pygame.K_g]: # test animations
            self.status = 'death'

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def get_status(self): 
        if self.direction.y < 0:
            self.status = 'jump'

        elif self.direction.y > 1: # 1 has to be bigger than gravity
            self.status = 'fall'

        else:
            if self.direction.x != 0:
                self.status = 'run'

            else:
                self.status = 'idle' # default animation

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
        self.run_dust_animation()