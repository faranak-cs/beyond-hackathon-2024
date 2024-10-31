from src.tomoyokai.hunger import Hunger
from src.sprites import AnimatedSprite


class Tomoyokai(AnimatedSprite):

    def __init__(self):
        super().__init__()
        self.hunger = Hunger()

    def update(self, delta_time):
        super().update(delta_time)
        self.hunger.update()
