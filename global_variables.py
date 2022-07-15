from random import randint

global game_state
game_state = 0

def get_game_state():
    return game_state

def set_game_state(state):
    global game_state
    game_state = state
    print(f"Game state was set: {game_state}")

def get_random_int(min, max):
    x = randint(min, max)
    # print(f"Random number: {x}")
    return x



