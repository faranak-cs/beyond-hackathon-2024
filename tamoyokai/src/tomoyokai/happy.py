from src.utils.timer import Timer
from random import randrange

HAPPY_SIZE = 5


class Happy(Timer):

    happiness = randrange(HAPPY_SIZE)

    def __init__(self):
        super().__init__(duration=5000, repeat=True, autostart=True, func=self.update_happiness)

    def update_happiness(self):
        if self.happiness > 0:
            self.happiness -= 1
        print("Happiness level:", self.happiness)

    def care(self):
        if self.happiness < HAPPY_SIZE:
            self.happiness += 1

    def get(self):
        return self.happiness
