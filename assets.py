import pygame


class Assets:
    def __init__(self):
        self.head_up = pygame.image.load("images/head_up.png").convert_alpha()
        self.head_down = pygame.image.load("images/head_down.png").convert_alpha()
        self.head_right = pygame.image.load("images/head_right.png").convert_alpha()
        self.head_left = pygame.image.load("images/head_left.png").convert_alpha()
        self.body_vertical = pygame.image.load("images/body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load("images/body_horizontal.png").convert_alpha()
        self.body_top_right = pygame.image.load("images/body_topright.png").convert_alpha()
        self.body_top_left = pygame.image.load("images/body_topleft.png").convert_alpha()
        self.body_bottom_right = pygame.image.load("images/body_bottomright.png").convert_alpha()
        self.body_bottom_left = pygame.image.load("images/body_bottomleft.png").convert_alpha()
        self.tail_up = pygame.image.load("images/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("images/tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load("images/tail_right.png").convert_alpha()
        self.tail_left = pygame.image.load("images/tail_left.png").convert_alpha()
        self.apple = pygame.image.load("images/apple.png").convert_alpha()
