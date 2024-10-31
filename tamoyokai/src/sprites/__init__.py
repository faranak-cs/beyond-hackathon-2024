from os.path import join

import pygame.sprite

from src import WINDOW_WIDTH
from src.settings import WINDOW_HEIGHT

all_sprites = pygame.sprite.Group()

class Drawable(pygame.sprite.Sprite):

    def __init__(self, pos, group):
        super().__init__(group)
        file_path = join("..", "resources", "animations", "Idle", "Idle1.png")
        print(file_path)
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_frect(topleft=pos)


class AnimatedSprite(Drawable):

    def __init__(self):
        super().__init__((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), all_sprites)