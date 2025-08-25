import random
from constants import WIDTH, HEIGHT, CELL_SIZE, SCORE_BAR_HEIGHT


class Food:
    def __init__(self, assets, snake_body):
        self.assets = assets

        self.position = None
        self.image = None
        self.name = None

        self.respawn(snake_body)
        self.randomize_food()

    def respawn(self, snake_body):
        # so later in the game when the snake gets bigger it will be very inefficient to find random spots every time,
        # so in the long run it'd be better to pass all positions available to random
        all_positions_available = []
        for x in range(0, WIDTH, CELL_SIZE):
            for y in range(SCORE_BAR_HEIGHT, HEIGHT, CELL_SIZE):
                if not (x, y) in snake_body:
                    all_positions_available.append((x, y))

        self.position = (random.choice(all_positions_available))

    def randomize_food(self):
        # returns a tuple (name: image) randomly
        # the point is in the future we can maybe add powerups for a particular
        # food based on our choice (key ---> name of food)
        self.name, self.image = random.choice(list(self.assets.food_images.items()))

    def draw(self, game_screen):
        game_screen.blit(self.image, self.position)
