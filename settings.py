
# Todo 
# - Add a way to change the settings via menu
# - Enemies
# - Sounds
# - Map design
# - Remaining animations

# Settings Variables

class Settings:
    def __init__(self):

        self.bg_color = (11, 9, 17)
        self.FPS = 60
        # self.TARGET_FPS = 60
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
        # self.screen_height = 768
        self.screen_height = len(self.test_level_map) * self.tile_size
        self.player_width = 19*3
        self.player_height = 22*3



# main_font = pygame.font.SysFont(None, 48) # criando uma fonte para o jogo

