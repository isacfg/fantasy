import pygame
import os
from settings import Settings

settings = Settings()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # calling the parent class constructor (Sprite)
        self.player_width = 50
        self.player_height = 68.75
        self.playerX = settings.screen_width / 2 - self.player_width / 2
        self.playerY = settings.screen_height / 2 - self.player_height / 2
        self.speed = 5

        self.test_player = pygame.image.load(os.path.join('assets', 'testPlayer.png'))
        self.test_player = pygame.transform.scale(self.test_player, (self.player_width, self.player_height))
        
        self.rect = self.test_player.get_rect()
        self.rect.center = (self.playerX, self.playerY)
 
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
        