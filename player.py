import pygame
import os
from settings import Settings

settings = Settings()
sourceFilDir = os.path.dirname(os.path.abspath(__file__))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # calling the parent class constructor (Sprite)
        self.player_width = 64
        self.player_height = 72
        self.playerX = settings.screen_width / 2 - self.player_width / 2
        self.playerY = settings.screen_height / 2 - self.player_height / 2
        self.speed = 5

        self.is_idle = True
        self.is_running = False

        # Load Idle Sprites
        self.idle_sprites = []
        for i in range(1, 7):
            self.idle_sprites.append(pygame.image.load(os.path.join(sourceFilDir, 'assets', 'player', 'idle', '0' + str(i) + '.png')))

        for i in range(len(self.idle_sprites)):
            self.idle_sprites[i] = pygame.transform.scale(self.idle_sprites[i], (self.player_width, self.player_height))
    
        # Load Running Sprites
        self.running_sprites = []
        for i in range(1, 7):
            self.running_sprites.append(pygame.image.load(os.path.join(sourceFilDir, 'assets', 'player', 'run', '0' + str(i) + '.png')))
        for i in range(len(self.running_sprites)):
            self.running_sprites[i] = pygame.transform.scale(self.running_sprites[i], (self.player_width, self.player_height))

        

        self.current_sprite = 0
        if self.is_idle == True:
            self.image = self.idle_sprites[int(self.current_sprite)]
        if self.is_running == True:
            self.image = self.running_sprites[int(self.current_sprite)]

        self.rect = self.image.get_rect()
        self.rect.center = (self.playerX, self.playerY)


    def animate(self):
        if self.is_idle == True:
            self.current_sprite += 0.15

            if self.current_sprite >= len(self.idle_sprites):
                self.current_sprite = 0

            self.image = self.idle_sprites[int(self.current_sprite)]

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        
        if keys[pygame.K_d]:
            self.rect.x += self.speed

    def update(self):
        self.get_input()
        self.animate()
        