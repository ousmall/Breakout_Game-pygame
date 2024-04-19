import pygame


def load_highest_score():
    try:
        with open('highest_score.txt') as f:
            return int(f.read())
    except FileNotFoundError:
        return 0


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = None
        self.image = None
        self.font = pygame.font.SysFont("Courier", 20)
        self.color = (255, 255, 255)
        self.lives = 3
        self.score = 0
        self.highest_score = load_highest_score()
        self.update_score()

    def update_score(self):
        text = f"Lives: {self.lives}     Highest Score: {self.highest_score}     Score: {self.score}"
        self.image = self.font.render(text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 30)
        if self.score >= self.highest_score:
            self.highest_score = self.score
            with open("highest_score.txt", "w") as f:
                f.write(str(self.highest_score))

    def current_score(self, points):
        self.score += points
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.update_score()

    def lose_life(self):
        self.lives -= 1
        self.update_score()

    def reset(self):
        self.score = 0
        self.lives = 3
        self.highest_score = load_highest_score()
        self.update_score()
