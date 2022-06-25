from operator import truediv
import pygame, sys
# Surfaces
# Plain color

# outside loop
screen = pygame.display.set_mode((800, 600))
test_surface = pygame.Surface((100, 100))
test_surface.fill('Red') # adding a color to the surface
image_surface = pygame.image.load('image.png') # loading an image

while True:

    screen.blit(test_surface, (0,0)) # surface, (x, y)
    screen.blit(image_surface, (0,0)) # surface, (x, y)

# creating text
# create a font (text size and style)
# write text on a surface
# blit the text surface

# outside loop
test_font = pygame.font.Font('assets/font/Font.ttf', 50) # font, size
text_surface = test_font.render('Hello World', False, 'Red') # text, antialias, color, for pixel art use False

while True:
    screen.blit(text_surface, (0,0)) # surface, (x, y)