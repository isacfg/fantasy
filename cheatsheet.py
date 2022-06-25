from operator import truediv
import pygame, sys
# Surfaces
# Plain color

# outside loop
screen = pygame.display.set_mode((800, 600))
test_surface = pygame.Surface((100, 100))
test_surface.fill('Red') # adding a color to the surface

while True:

    screen.blit(test_surface, (0,0)) # surface, (x, y)