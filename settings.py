from random_map import generate_random_map

class Settings:
    def __init__(self):

        self.bg_color = (11, 9, 17) # background color
        self.FPS = 60
        self.MENU_FPS = 30
        self.game_name = "Fantasy"
        self.game_version = "0.0.1"
        self.game_authors = "Isaac F. e Israel S."

        # Mapa aleatorio
        
        self.test_level_map = generate_random_map()

        self.tile_size = 48
        self.screen_width = 1200
        self.screen_height = 700
        self.player_width = 19*3
        self.player_height = 22*3 # proporção original 19/22




