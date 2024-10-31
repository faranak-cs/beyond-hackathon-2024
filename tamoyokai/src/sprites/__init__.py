from os.path import join

import pygame.sprite


class Drawable(pygame.sprite.Sprite):

    def __init__(self, sprites, pos):
        super().__init__(sprites)
        file_path = join("..", "resources", "animations", "Idle", "Idle1.png")
        print(file_path)
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_frect(topleft=pos)
