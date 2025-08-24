import pygame
import sys
import time
from constants import WIDTH, HEIGHT, BLACK, FPS, WHITE, BLUE
from assets import Assets
from food import Food
from snakebody import SnakeBody

pygame.init()

pygame.display.set_caption("S'Nake")
game_screen = pygame.display.set_mode((WIDTH, HEIGHT))

# font to show the score
score = 0
font_score = pygame.font.SysFont("arial", 30)
font_game_over = pygame.font.SysFont("times new roman", 50, False, True)

clock = pygame.time.Clock()

# TODO add grid, more fruit. make sure the snake cant touch the score

assets = Assets()
apple = Food(assets)
snake_body = SnakeBody([(60, 60), (40, 60), (20, 60)], assets)
direction_change_to = "RIGHT"


def check_violation():
    x, y = snake_body.head
    # boundaries (WIDTH and HEIGHT are up to their value -1 according to game_screen.
    # snake moves by 20 pixels so the at 720 it's a violation)
    # check if snake runs into itself
    return (
        x >= WIDTH or x < 0 or
        y >= HEIGHT or y < 0 or
        snake_body.head in snake_body.body[1:]
    )


def show_score():
    surface_font = font_score.render(f"score is {score}", True, WHITE)
    score_rect = surface_font.get_rect()

    game_screen.blit(surface_font, score_rect)


def game_over():
    surface_font = font_score.render(f"your final score is {score}", True, BLUE)
    score_rect = surface_font.get_rect(midtop=(WIDTH // 2, 200))

    game_screen.blit(surface_font, score_rect)
    pygame.display.flip()
    time.sleep(2)


def update_game():
    global score
    # check collision first then move the snake
    if apple.position == snake_body.head:
        apple.respawn()
        snake_body.grow = True
        score += 1

    snake_body.move()


def draw_game():
    game_screen.fill(BLACK)
    snake_body.draw(game_screen)
    apple.draw(game_screen)
    show_score()
    pygame.display.flip()


# --- main ---
game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # get out of the loop
            game_running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
            elif event.key == pygame.K_UP:
                direction_change_to = "UP"
            elif event.key == pygame.K_DOWN:
                direction_change_to = "DOWN"
            elif event.key == pygame.K_RIGHT:
                direction_change_to = "RIGHT"
            elif event.key == pygame.K_LEFT:
                direction_change_to = "LEFT"

    if check_violation():
        game_running = False
        break

    snake_body.change_direction(direction_change_to)
    update_game()

    draw_game()
    clock.tick(FPS)

game_over()

pygame.quit()
sys.exit()
