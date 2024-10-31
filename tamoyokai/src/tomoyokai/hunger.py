from src.utils.timer import Timer
from random import randrange

BELLY_SIZE = 5


class Hunger(Timer):

    belly = randrange(BELLY_SIZE)

    def __init__(self):
        super().__init__(duration=5000, repeat=True, autostart=True, func=self.update_belly)

    def update_belly(self):
        if self.belly > 0:
            self.belly -= 1
        print("Belly level:", self.belly)

    def feed(self):
        if self.belly < BELLY_SIZE:
            self.belly += 1

    def get(self):
        return self.belly
