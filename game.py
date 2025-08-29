import pygame
import sys
import time
from constants import *
from assets import Assets
from food import Food
from snakebody import SnakeBody

pygame.init()

pygame.display.set_caption("S'Nake")
game_screen = pygame.display.set_mode((WIDTH, HEIGHT))

# font to show the score
score = 0
font_score = pygame.font.SysFont("arial", 30)
font_game_over = pygame.font.SysFont("Monospace", 50, True, True)

clock = pygame.time.Clock()

assets = Assets()

# give default coordinates based on CELL_SIZE which is 20 pixels
snake_body = SnakeBody([(60, 60), (40, 60), (20, 60)], assets)

# Food to appear in game
food = Food(assets, snake_body.body)

direction_change_to = "RIGHT"


def check_game_over():
    x, y = snake_body.head
    # boundaries (WIDTH and HEIGHT are up to their value -1 according to game_screen.
    # snake moves by 20 pixels so the at 720 it's a violation)
    # check if snake runs into itself
    return (
        x >= WIDTH or x < 0 or
        y >= HEIGHT or y < SCORE_BAR_HEIGHT or
        snake_body.head in snake_body.body[1:] or
        check_victory()
    )


def show_score():
    pygame.draw.rect(game_screen, WHITE, (0, 0, WIDTH, SCORE_BAR_HEIGHT))

    surface_font = font_score.render(f"score is {score}", True, LIGHT_BLUE)
    text_rect = surface_font.get_rect(center=(WIDTH // 2, SCORE_BAR_HEIGHT // 2))

    game_screen.blit(surface_font, text_rect)


def game_over():
    if check_victory():
        surface_font = font_score.render(f"You Wonnnn! your overall score is {score}", True, GOLD)
    else:
        surface_font = font_score.render(f"your final score is {score}", True, BODY_COLOR)

    score_rect = surface_font.get_rect(midtop=(WIDTH // 2, 200))
    game_screen.blit(surface_font, score_rect)
    pygame.display.flip()
    time.sleep(2)


def check_victory():
    return len(snake_body.body) >= CELLS


def update_game():
    global score
    # check collision first then move the snake
    if food.position == snake_body.head:
        food.respawn(snake_body.body)
        food.randomize_food()
        snake_body.grow = True
        score += 1

    snake_body.move()


def add_grid():
    for column in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(game_screen, LIGHT_GREEN, (column, SCORE_BAR_HEIGHT), (column, HEIGHT))

    # I want to make the first line red so that to display the border of the score rectangle
    pygame.draw.line(game_screen, RED, (0, SCORE_BAR_HEIGHT), (WIDTH, SCORE_BAR_HEIGHT), 2)

    for stripe in range(SCORE_BAR_HEIGHT + CELL_SIZE, HEIGHT, CELL_SIZE):
        pygame.draw.line(game_screen, LIGHT_GREEN, (0, stripe), (WIDTH, stripe))


def draw_game():
    game_screen.fill(BLACK)
    add_grid()
    snake_body.draw(game_screen)
    food.draw(game_screen)
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
                break
            elif event.key == pygame.K_UP:
                direction_change_to = "UP"
            elif event.key == pygame.K_DOWN:
                direction_change_to = "DOWN"
            elif event.key == pygame.K_RIGHT:
                direction_change_to = "RIGHT"
            elif event.key == pygame.K_LEFT:
                direction_change_to = "LEFT"

    if check_game_over():
        game_running = False
        break

    snake_body.change_direction(direction_change_to)
    update_game()

    draw_game()
    clock.tick(FPS)

game_over()

pygame.quit()
sys.exit()
