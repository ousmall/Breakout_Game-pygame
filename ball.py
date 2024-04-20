import pygame
import random

BALL_ORIGIN = (400, 600)
BALL_RADIUS = 10
WHITE = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = None
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = BALL_ORIGIN
        self.initial_direction()

    def initial_direction(self):
        x_velocity = 5 * random.choice([1, -1])
        y_velocity = -5
        self.velocity = [x_velocity, y_velocity]

    def move(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def x_bounce(self):
        self.velocity[0] *= -1

    def y_bounce(self):
        self.velocity[1] *= -1

    def reset(self):
        self.rect.center = BALL_ORIGIN
        self.initial_direction()

    def check_collision(self, paddle, blocks, scoreboard):
        for block in blocks:
            if self.rect.colliderect(block.rect):
                if not block.hit:
                    block.hit = True
                    blocks.remove(block)
                    scoreboard.current_score()

        if self.rect.colliderect(paddle.rect):
            self.y_bounce()

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.x_bounce()

        if self.rect.top <= 0:
            self.y_bounce()
        elif self.rect.bottom > SCREEN_HEIGHT:
            scoreboard.lose_life()
            self.reset()
