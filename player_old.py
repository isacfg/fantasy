import pygame, os
from settings import Settings

settings = Settings()
sourceFilDir = os.path.dirname(os.path.abspath(__file__))

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__() # calling the parent class constructor (Sprite)
        self.player_width = 16 * 16
        self.player_height = 18 * 16

        self.animation_speed = 0.225
        self.speed = 4

    
        # Animation Variables
        self.is_idle = True
        self.is_running_right = False
        self.is_running_left = False
        self.is_jumping = False

        self.load_sprites()


        self.current_sprite = 0

        # testar simplificação
        if self.is_idle == True:
            self.image = self.idle_sprites[int(self.current_sprite)]
        if self.is_running_right == True:
            self.image = self.running_sprites_right[int(self.current_sprite)]
        if self.is_running_left == True:
            self.image = self.running_sprites_left[int(self.current_sprite)]
        if self.is_jumping == True:
            self.image = self.jump_sprites[int(self.current_sprite)]

        self.rect = self.image.get_rect(topleft = pos)

    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


    def animate(self):
        if self.is_idle == True:
            self.current_sprite += self.animation_speed

            if self.current_sprite >= len(self.idle_sprites):
                self.current_sprite = 0

            self.image = self.idle_sprites[int(self.current_sprite)]
        
        if self.is_running_right == True:
            self.current_sprite += self.animation_speed

            if self.current_sprite >= len(self.running_sprites_right):
                self.current_sprite = 0

            self.image = self.running_sprites_right[int(self.current_sprite)]

        if self.is_running_left == True:
            self.current_sprite += self.animation_speed

            if self.current_sprite >= len(self.running_sprites_left):
                self.current_sprite = 0

            self.image = self.running_sprites_left[int(self.current_sprite)]

        if self.is_jumping == True:
            self.current_sprite += self.animation_speed

            if self.current_sprite >= len(self.jump_sprites):
                self.current_sprite = 0
                self.is_jumping = False

            self.image = self.jump_sprites[int(self.current_sprite)]
   
    
    def get_input(self):
        keys = pygame.key.get_pressed()

        # if keys[pygame.K_w]:
        #     self.rect.y -= self.speed

        #     self.is_idle = True
        #     self.is_running_right = False
        #     self.is_running_left = False
        #     self.is_jumping = False
        
        # if keys[pygame.K_s]:
        #     self.rect.y += self.speed

        #     self.is_idle = True
        #     self.is_running_right = False
        #     self.is_running_left = False
        #     self.is_jumping = False
        
        if keys[pygame.K_a]:
            self.rect.x -= self.speed

            self.is_idle = False
            self.is_running_right = False
            self.is_running_left = True
            self.is_jumping = False
        
        if keys[pygame.K_d]:
            self.rect.x += self.speed

            self.is_idle = False
            self.is_running_right = True
            self.is_running_left = False
            self.is_jumping = False

        if keys[pygame.K_SPACE]:

            self.is_idle = False
            self.is_running_right = False
            self.is_running_left = False
            self.is_jumping = True

    def update(self, deltaTime):
        # self.get_input()
        # self.animate()
        pass

    def load_sprites(self):
        # Load Idle Sprites
        self.idle_sprites = []
        for i in range(1, 7):
            self.idle_sprites.append(pygame.image.load(os.path.join(sourceFilDir, 'assets\player\idle\knight (' + str(i) + ').png')))
        
        for i in range(len(self.idle_sprites)):
            self.idle_sprites[i] = pygame.transform.scale(self.idle_sprites[i], (self.player_width, self.player_height))
    


        # Load Running Sprites Right
        self.running_sprites_right = []
        for i in range(1, 9):
            self.running_sprites_right.append(pygame.image.load(os.path.join(sourceFilDir, 'assets\player\k_run\knight (' + str(i) + ').png')))

        for i in range(len(self.running_sprites_right)):
            self.running_sprites_right[i] = pygame.transform.scale(self.running_sprites_right[i], (self.player_width, self.player_height))

        # Load Running Sprites Left
        self.running_sprites_left = []
        self.running_sprites_left = self.running_sprites_right[:]
        for i in range(len(self.running_sprites_left)):
            self.running_sprites_left[i] = pygame.transform.flip(self.running_sprites_left[i], True, False)
        
        # Load Jump Sprites
        self.jump_sprites = []
        for i in range(1, 13):
            self.jump_sprites.append(pygame.image.load(os.path.join(sourceFilDir, 'assets\player\jump\knight (' + str(i) + ').png')))
        
        for i in range(len(self.jump_sprites)):
            self.jump_sprites[i] = pygame.transform.scale(self.jump_sprites[i], (self.player_width, self.player_height))