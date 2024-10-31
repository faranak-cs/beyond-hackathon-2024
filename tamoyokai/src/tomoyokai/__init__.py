from os import walk
from os.path import join

import pygame

from src import WINDOW_WIDTH, WINDOW_HEIGHT, all_sprites
from src.tomoyokai.hunger import Hunger
from src.tomoyokai.happy import Happy

class Tomoyokai(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__(all_sprites)

        self.animation_speed = 5
        self.frames = self.import_frames()
        self.status = 'Idle'
        self.frame_index = 0

        # general setup
        self.image = self.frames[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        self.hunger = Hunger()
        self.happy = Happy()

    def update(self, dt):
        self.animate(dt)
        self.hunger.update()
        self.happy.update()

    def import_frames(self):
        frames = {'Idle': []}

        for state in frames.keys():
            for folder_path, _, file_names in walk(join("..", "resources", "animations", state)):
                for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                    full_path = join(folder_path, file_name)
                    surface = pygame.image.load(full_path).convert_alpha()
                    frames[state].append(surface)
        return frames

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        if self.frame_index >= len(self.frames[self.status]):
            self.frame_index = 0

        self.image = self.frames[self.status][int(self.frame_index)]