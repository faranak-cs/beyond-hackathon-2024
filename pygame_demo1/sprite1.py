import pygame, sys
from pygame.locals import *
import random
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SPRITE_SIZE = (128, 128) 

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
 
class Monster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.set_image("monster.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 

    def set_image(self, filename):
        raw_image = pygame.image.load(filename)
        self.image = pygame.transform.scale(raw_image, SPRITE_SIZE)
 
    def move(self, direction):
        self.rect.move_ip(*direction)
        if (self.rect.bottom < 0):
            self.rect.top = SCREEN_HEIGHT
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.bottom = 0
        if (self.rect.right < 0):
            self.rect.left = SCREEN_WIDTH
        if (self.rect.left > SCREEN_WIDTH):
            self.rect.right = 0
 
    def draw(self, surface):
        surface.blit(self.image, self.rect) 

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.move((0, -10))
        if pressed_keys[K_DOWN]:
            self.move((0, 10))
        if pressed_keys[K_LEFT]:
            self.move((-10, 0))
        if pressed_keys[K_RIGHT]:
            self.move((10, 0))
         
monster = Monster()

while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    monster.update()
     
    DISPLAYSURF.fill(WHITE)
    monster.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)
