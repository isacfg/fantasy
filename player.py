import pygame, os
from settings import Settings

settings = Settings()
sourceFilDir = os.path.dirname(os.path.abspath(__file__))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # calling the parent class constructor (Sprite)
        self.player_width = 16 * 16
        self.player_height = 18 * 16
        self.playerX = settings.screen_width / 2 - self.player_width / 2
        self.playerY = settings.screen_height / 2 - self.player_height / 2

        self.speed = 2.5
        self.animation_speed = 0.15

        # Physics
        self.gravity = 0.6
        self.friction = -0.2 # lower more slippery
        self.max_velocity_x = 10
        self.max_velocity_y = 7
        self.acceleration_in_x = 1.4
        self.jump_speed = -16
        self.on_ground = False
        self.ground = 500 # temporary ground level
        self.position = pygame.math.Vector2(self.playerX, self.playerY)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, self.gravity)
        
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

        self.rect = self.image.get_rect()
        self.rect.center = (self.playerX, self.playerY)

    
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

        if keys[pygame.K_w]:
            self.rect.y -= self.speed

            self.is_idle = True
            self.is_running_right = False
            self.is_running_left = False
            self.is_jumping = False
        
        if keys[pygame.K_s]:
            self.rect.y += self.speed

            self.is_idle = True
            self.is_running_right = False
            self.is_running_left = False
            self.is_jumping = False
    


    def horizontal_movement(self, deltaTime):
        keys = pygame.key.get_pressed() 
        self.acceleration.x = 0

        if keys[pygame.K_a]:
            self.acceleration.x -= self.acceleration_in_x

            self.is_idle = False
            self.is_running_right = False
            self.is_running_left = True
            self.is_jumping = False
        
        if keys[pygame.K_d]:
            self.acceleration.x += self.acceleration_in_x

            self.is_idle = False
            self.is_running_right = True
            self.is_running_left = False
            self.is_jumping = False        

        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * deltaTime
        self.limit_velocity(self.max_velocity_x)
        self.position.x += self.velocity.x * deltaTime + (self.acceleration.x * 0.5) * deltaTime ** 2
        self.rect.x = self.position.x

    def vertical_movement(self, deltaTime):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.jump()

        self.velocity.y += self.acceleration.y * deltaTime
        if self.velocity.y > self.max_velocity_y: self.velocity.y = self.max_velocity_y # limit max velocity

        self.position.y += self.velocity.y * deltaTime + (self.acceleration.y * 0.5) * deltaTime ** 2
        if self.position.y > self.ground: # limitar o player para o chão
            self.on_ground = True
            self.position.y = self.ground
            self.velocity.y = 0

        self.rect.bottom = self.position.y

    def jump(self):

        if self.on_ground:
            self.velocity.y = self.jump_speed
            self.on_ground = False

            self.is_idle = False
            self.is_running_right = False
            self.is_running_left = False
            self.is_jumping = True

    def limit_velocity(self, max_vel):
        self.velocity.x = max(-max_vel, min(self.velocity.x, max_vel))
        if abs(self.velocity.x) < 0.01: self.velocity.x = 0

    def update(self, deltaTime):
        # self.get_input()
        self.horizontal_movement(deltaTime)
        self.vertical_movement(deltaTime)
        self.animate()


        

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