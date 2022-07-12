from os import walk
import pygame
from settings import Settings

settings = Settings()

# Todo:
# - If usar pixel pefect colision, mudar a função para receber mascaras
# - Gerar uma mascara para cara sprite, retornar em uma lsita separada, e adicionar ao dic

def import_folder(path, needs_to_scale = False):
    lista = []
    
    for _,__,img_files in walk(path): # walk(path) dirpath, dirnames, filenames)
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha() # convert_alpha() is needed to make the image transparent
            if needs_to_scale: # util pq particulas nao precisam ser escaladas
                # mudar referencias em player para settings.player_width e settings.player_height
                image_surf = pygame.transform.scale(image_surf, (settings.player_width, settings.player_height))

            lista.append(image_surf)

    return lista


def import_tiles(path):
    pass