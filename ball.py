import pygame
import random

BALL_ORIGIN = (400, 650)
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
        x_velocity = 5 * random.choice([-1, 1])
        y_velocity = -5 * random.choice([-1, 1])
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
            # 检查球与砖块的碰撞
            if self.rect.colliderect(block.rect):

                blocks.remove(block)

                color = block.color
                if color == "red":
                    score = 4
                elif color == "orange":
                    score = 3
                elif color == "yellow":
                    score = 2
                else:
                    score = 1  # green is 1
                scoreboard.current_score(score)

        if self.rect.colliderect(paddle.rect):
            self.y_bounce()

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.x_bounce()

        if self.rect.top <= 0:
            self.y_bounce()
        elif self.rect.bottom > SCREEN_HEIGHT:
            scoreboard.lose_life()
            self.reset()
