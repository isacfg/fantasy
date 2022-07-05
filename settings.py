

class Settings:
    def __init__(self):

        self.bg_color = (11, 9, 17)
        self.FPS = 60
        self.game_name = "Fantasy"
        self.game_version = "0.0.1"
        self.game_authors = "Isaac F. e Israel S."

        self.test_level_map = [
        '                            ', #1
        '                            ', #2 
        '                            ', #3 
        ' XX    XXX            XX    ', #4
        ' XX P                       ', #5 
        ' XXXX         XX         XX ',# 6
        ' XXXX       XX              ',# 7
        ' XX    X  XXXX    XX  XX    ', #8 
        '       X  XXXX    XX  XXX   ',# 9
        '    XXXX  XXXXXX  XX  XXXX  ', #10
        'XXXXXXXX  XXXXXX  XX  XXXX  '] #11


        self.tile_size = 64
        self.screen_width = 1200
        self.screen_height = 700
        self.player_width = 19*3
        self.player_height = 22*3




