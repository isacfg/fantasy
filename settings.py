
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

        # self.test_level_map = [
        # '                            ', 1
        # '                            ', 2 
        # '                            ', 3 
        # ' XX    XXX            XX    ', 4
        # ' XX P                       ', 5 
        # ' XXXX         XX         XX ', 6
        # ' XXXX       XX              ', 7
        # ' XX    X  XXXX    XX  XX    ', 8 
        # '       X  XXXX    XX  XXX   ', 9
        # '    XXXX  XXXXXX  XX  XXXX  ', 10
        # 'XXXXXXXX  XXXXXX  XX  XXXX  '] 11

        self.test_level_map = [
        '                                          ', #1
        '                                          ', #2 
        '                                          ', #3 
        ' X     XXXXXXXX         XXXX        XXXXXX', #4
        '   X                                      ', #3 
        '                   XX              X      ',
        '   X P         XX                         ', #5 
        '  XXX                    XXXXXXXXX        ', #6
        ' XXXX                                     ',
        ' XXXX       XX                            ', #7
        '  X    X  XXXX    XX  XXXXXX     XXXXXXXX', #8 
        '       X  XX      XX  XXX     XXXXXXXXXXX', #9
        '    XXXX  XXXXXX  XX  XXXX    XXXXXXXXXXXX', #10
        'XXXXXXXX  XXXXXX  XX  XXXXXX  XXXXXXXXXXXX'] #11
  

        self.tile_size = 52
        self.screen_width = 1200
        self.screen_height = 700
        # self.screen_height = len(self.test_level_map) * self.tile_size
        self.player_width = 19*3
        self.player_height = 22*3



# main_font = pygame.font.SysFont(None, 48) # criando uma fonte para o jogo

