import pygame

from src import WINDOW_WIDTH, WINDOW_HEIGHT, all_sprites
from src.tomoyokai.hunger import Hunger
from src.sprites import assets

class Tomoyokai(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__(all_sprites)

        self.import_assets()
        self.status = 'Idle'
        self.frame_index = 0

        # general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        self.hunger = Hunger()
        self.happy = Happy()

    def update(self, dt):
        self.animate(dt)
        self.hunger.update()
        self.happy.update()

    def import_assets(self):
        self.animations = {'Idle': []}

        for animation in self.animations.keys():
            self.animations[animation] = assets.import_folder("..", "resources", "animations")


    def animate(self,dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]