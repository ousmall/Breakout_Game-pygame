import pygame

BLOCK_WIDTH = 50
BLOCK_HEIGHT = 20
BLOCK_SPACE = 5
BLOCK_COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0)]
BLOCK_ROWS = 8


class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((BLOCK_WIDTH, BLOCK_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hit = False


class BlockManager:
    def __init__(self):
        self.blocks = []
        self.create_blocks()

    def create_blocks(self):
        start_y = 80
        for row in range(BLOCK_ROWS):
            color_index = row // 2
            color = BLOCK_COLORS[color_index]
            for col in range(50, 750, BLOCK_WIDTH + BLOCK_SPACE):
                block = Block(color, col, start_y + row * (BLOCK_HEIGHT + BLOCK_SPACE))
                self.blocks.append(block)
