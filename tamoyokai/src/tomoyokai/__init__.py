from src.tomoyokai.hunger import Hunger
from src.tomoyokai.happy import Happy
from src.sprites import AnimatedSprite


class Tomoyokai(AnimatedSprite):

    def __init__(self):
        super().__init__()
        self.hunger = Hunger()
        self.happy = Happy()

    def update(self, delta_time):
        super().update(delta_time)
        self.hunger.update()
        self.happy.update()
