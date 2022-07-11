

class Settings:
    def __init__(self):

        self.bg_color = (11, 9, 17) # background color
        self.FPS = 60
        self.game_name = "Fantasy"
        self.game_version = "0.0.1"
        self.game_authors = "Isaac F. e Israel S."

        self.test_level_map = [
        '                            ', #1
        '                            ', #2
        '                            ', #3
        '                            ', #4
        '                            ', #5
        '     XX           XXX            ', #6
        '              X              ', #7
        'XX      XX      XX       XX         ', #8
        'P                     X       ', #9
        'XXXXXXXX XXXXXXXXXX XXXXXXXX', #10
        'XXXXXXXX XXXXXXXXXX XXXXXXXX', #11
        ]

        self.tile_size = 64
        self.screen_width = 1200
        self.screen_height = 700
        self.player_width = 19*3
        self.player_height = 22*3 # proporção original 19/22




