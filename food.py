import random
from constants import WIDTH, HEIGHT, CELL_SIZE


class Food:
    def __init__(self, assets):
        self.assets = assets
        self.position = None
        self.respawn()

    def respawn(self):
        # (x, y)
        self.position = (random.randrange(0, (WIDTH // CELL_SIZE)) * CELL_SIZE,
                         random.randrange(0, (HEIGHT // CELL_SIZE)) * CELL_SIZE)

    def draw(self, game_screen):
        game_screen.blit(self.assets.apple, self.position)
