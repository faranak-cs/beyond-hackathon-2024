import pygame
from hunger import Hunger


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Tomoyokai')
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.hunger = Hunger()

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.hunger.feed()

            # update
            self.all_sprites.update(dt)

            # draw
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
            self.hunger.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()