# Working with sprites
import pygame, sys, os

class Rect(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(os.path.join('assets', 'testPlayer.png'))
        self.image = pygame.transform.scale(self.image, (50, 68.75))
        self.rect = self.image.get_rect()

pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

rect = Rect()
rect_group = pygame.sprite.Group()
rect_group.add(rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.flip()
    rect_group.draw(screen)
    clock.tick(60)