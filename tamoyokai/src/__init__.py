import pygame

from src.utils.settings import WINDOW_WIDTH, WINDOW_HEIGHT
from src.sprites import all_sprites
from src.tomoyokai import Tomoyokai


class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Tomoyokai')
        self.clock = pygame.time.Clock()
        self.running = True

        self.tomoyokai = Tomoyokai()

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.tomoyokai.hunger.feed()

            # update
            all_sprites.update(dt)

            # update the timer
            self.hunger.update()

            # draw
            all_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()