from os import walk
import pygame
from settings import Settings

settings = Settings()

def import_folder(path):
    surface_list = []
    
    for _,__,img_files in walk(path): # walk(path) returns a tuple of 3 elements: (dirpath, dirnames, filenames)
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha() # convert_alpha() is needed to make the image transparent
            image_surf = pygame.transform.scale(image_surf, (settings.player_width, settings.player_height))
            surface_list.append(image_surf)

    return surface_list