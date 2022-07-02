global game_state
game_state = 0

def get_game_state():
    return game_state

def set_game_state(state):
    global game_state
    game_state = state