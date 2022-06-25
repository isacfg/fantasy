import pygame
import os
from settings import Settings


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.test_player = pygame.image.load(os.path.join('assets', 'testPlayer.png'))
        self.test_player = pygame.transform.scale(self.test_player, (50, 68.75))
        self.rect = self.test_player.get_rect()
        self.speed = 5
 
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
        pass