import pygame.sprite

all_sprites = pygame.sprite.Group()

class Drawable(pygame.sprite.Sprite):

    def __init__(self, surface, pos, group):
        super().__init__(group)
        self.image = surface
        self.rect = self.image.get_frect(topleft=pos)


class AnimatedSprite(Drawable):

    def __init__(self, frames, pos):
        super().__init__(frames[0], pos, all_sprites)
        self.state = 'Idle'
        self.animations = frames
        self.frame_index = 0

    def animate(self,dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.state]):
            self.frame_index = 0

        self.image = self.animations[self.state][int(self.frame_index)]