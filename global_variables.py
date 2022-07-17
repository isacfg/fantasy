from random import randint

import pygame, sys

# Iniciando fontes
pygame.font.init()


# menu functions
global game_state
game_state = 0

def get_game_state():
    return game_state

def set_game_state(state):
    global game_state
    game_state = state
    print(f"Game state was set: {game_state}")


# random map
def get_random_int(min, max):
    x = randint(min, max)
    # print(f"Random number: {x}")
    return x


# text
font_name = './assets/fonts/PressStart2P-Regular.ttf'
def draw_text(text,color,x,y, font_size, screen, debug = False): 
    font = pygame.font.Font(font_name, font_size) # fontname, size

    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_obj, text_rect)
    if debug:
        print(f"draw text was called: {text}")

global start_ticks
start_ticks = 0
global seconds
seconds = 0

def start_time():
    start_ticks = pygame.time.get_ticks()


def get_time():
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    seconds = round(seconds, 1)

    return seconds   


def reset_time():
    global start_ticks
    start_ticks = pygame.time.get_ticks()

# player
# global is_player_dead
# is_player_dead = False

# def get_is_player_dead():
#     return is_player_dead

# def set_is_player_dead(state):
#     global is_player_dead
#     is_player_dead = state
#     print(f"Player is dead: {is_player_dead}")