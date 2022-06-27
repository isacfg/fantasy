
# Settings Variables

class Settings:
    def __init__(self):

        self.bg_color = (32, 32, 32)
        self.FPS = 60
        self.TARGET_FPS = 60
        self.game_name = "Fantasy"
        self.game_version = "0.0.1"
        self.game_authors = "Isaac F. e Israel S."

        self.test_level_map = [
        '                            ',
        '                            ',
        '                            ',
        ' XX    XXX            XX    ',
        ' XX P                       ',
        ' XXXX         XX         XX ',
        ' XXXX       XX              ',
        ' XX    X  XXXX    XX  XX    ',
        '       X  XXXX    XX  XXX   ',
        '    XXXX  XXXXXX  XX  XXXX  ',
        'XXXXXXXX  XXXXXX  XX  XXXX  ']

        self.tile_size = 64
        self.screen_width = 1200
        # self.screen_height = 680
        self.screen_height = len(self.test_level_map) * self.tile_size



# main_font = pygame.font.SysFont(None, 48) # criando uma fonte para o jogo

