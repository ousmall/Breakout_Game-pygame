import pygame

PADDLE_ORIGIN = (400, 670)


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 20))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = PADDLE_ORIGIN

    def move_right(self):
        self.rect.x += 20
        if self.rect.right > 800:
            self.rect.right = 800

    def move_left(self):
        self.rect.x -= 20
        if self.rect.left < 0:
            self.rect.left = 0

    def reset(self):
        self.rect.center = PADDLE_ORIGIN
