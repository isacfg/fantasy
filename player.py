import pygame
import os
from settings import Settings


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.test_player = pygame.image.load(os.path.join('assets', 'testPlayer.png'))
        self.test_player = pygame.transform.scale(self.test_player, (50, 50))
        self.rect = self.test_player.get_rect()
 
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= 10
        
        if keys[pygame.K_s]:
            self.rect.y += 10
        
        if keys[pygame.K_a]:
            self.rect.x -= 10
        
        if keys[pygame.K_d]:
            self.rect.x += 10

    def update(self):
        self.get_input()
        pass