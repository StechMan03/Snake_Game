from constants import CELL_SIZE


class SnakeBody:
    def __init__(self, body, assets):
        self.body = body
        self.assets = assets
        self.grow = False
        self.current_direction = "RIGHT"

    @property
    def head(self):
        return self.body[0]

    def change_direction(self, change_direction):
        # prevent reversing into itself
        opposite = {"RIGHT": "LEFT", "UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT"}
        if change_direction != opposite.get(self.current_direction):
            self.current_direction = change_direction

    def move(self):
        new_head = None
        x, y = self.head
        if self.current_direction == "RIGHT":
            new_head = (x + CELL_SIZE, y)
        elif self.current_direction == "LEFT":
            new_head = (x - CELL_SIZE, y)
        elif self.current_direction == "UP":
            new_head = (x, y - CELL_SIZE)
        elif self.current_direction == "DOWN":
            new_head = (x, y + CELL_SIZE)

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self, game_screen):
        image = None

        # --- head ---
        if self.current_direction == "UP":
            image = self.assets.head_up
        elif self.current_direction == "DOWN":
            image = self.assets.head_down
        elif self.current_direction == "RIGHT":
            image = self.assets.head_right
        elif self.current_direction == "LEFT":
            image = self.assets.head_left
        game_screen.blit(image, self.body[0])

        for i in range(1, len(self.body) - 1):
            curr_x, curr_y = self.body[i]
            prev_x, prev_y = self.body[i - 1]
            next_x, next_y = self.body[i + 1]

            # --- body ---
            if next_x == prev_x:
                image = self.assets.body_vertical
            elif next_y == prev_y:
                image = self.assets.body_horizontal
            elif (curr_x > prev_x and curr_y > next_y) or (curr_x < next_x and curr_y > prev_y):
                image = self.assets.body_bottom_left
            elif (curr_x > prev_x and curr_y < next_y) or (curr_x < next_x and curr_y < prev_y):
                image = self.assets.body_top_left
            elif (curr_x < prev_x and curr_y > next_y) or (curr_x > next_x and curr_y > prev_y):
                image = self.assets.body_bottom_right
            elif (curr_x < prev_x and curr_y < next_y) or (curr_x > next_x and curr_y < prev_y):
                image = self.assets.body_top_right
            game_screen.blit(image, (curr_x, curr_y))

        # --- tail ---
        # snake can only move on the X or Y axis not diagonally
        # if the tail is at the same direction as next we don't blit a new direction
        tail_x, tail_y = self.body[-1]
        prev_x, prev_y = self.body[-2]
        if tail_x > prev_x:
            image = self.assets.tail_left
        elif tail_x < prev_x:
            image = self.assets.tail_right
        elif tail_y > prev_y:
            image = self.assets.tail_down
        elif tail_y < prev_y:
            image = self.assets.tail_up
        game_screen.blit(image, (tail_x, tail_y))
