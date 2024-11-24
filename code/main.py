from settings import *
from player import Player

class Game:
    def __init__(self):
        # Setup
        pygame.init()
        self.displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Vampire Survivor')
        self.clock = pygame.time.Clock()
        self.running = True

        # Groups
        self.allSprites = pygame.sprite.Group()

        # Sprites
        self.player = Player((WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2), self.allSprites)

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.allSprites.update(dt)
            self.displaySurface.fill((0,0,0))
            self.allSprites.draw(self.displaySurface)

            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
