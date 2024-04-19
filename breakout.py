import pygame
from blocks import BlockManager
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard

# initial Pygame
pygame.init()

# setup interface
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout Game")

# colors & font
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT_1 = pygame.font.SysFont("Courier", 26)
FONT_2 = pygame.font.SysFont("Courier", 20)

# create objects
block_manager = BlockManager()
block_manager.create_blocks()

paddle = Paddle()
ball = Ball()
score_board = Scoreboard()
clock = pygame.time.Clock()

# global sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(paddle, ball, score_board)


def show_game_over():
    game_over_text = FONT_1.render("Game Over", True, WHITE)
    click_text = FONT_2.render("Click to choose", True, WHITE)
    quit_text = FONT_2.render("Quit", True, WHITE)
    restart_text = FONT_2.render("Restart", True, WHITE)

    game_over_text_pos = ((SCREEN_WIDTH - game_over_text.get_width()) // 2, SCREEN_HEIGHT // 2 - 50)
    click_text_pos = ((SCREEN_WIDTH - click_text.get_width()) // 2, SCREEN_HEIGHT // 2)
    quit_text_pos = ((SCREEN_WIDTH - quit_text.get_width()) // 2 - 75, SCREEN_HEIGHT // 2 + 50)
    restart_text_pos = ((SCREEN_WIDTH - restart_text.get_width()) // 2 + 75, SCREEN_HEIGHT // 2 + 50)

    screen.blit(game_over_text, game_over_text_pos)
    screen.blit(click_text, click_text_pos)
    screen.blit(quit_text, quit_text_pos)
    screen.blit(restart_text, restart_text_pos)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if quit_text.get_rect(topleft=quit_text_pos).collidepoint(mouse_pos):
                    pygame.quit()
                    return False  # quit the game
                elif restart_text.get_rect(topleft=restart_text_pos).collidepoint(mouse_pos):
                    return True  # restart the game


# main loop
def play_game():
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # move paddle
        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddle.move_left()
            if keys[pygame.K_RIGHT]:
                paddle.move_right()

            # ball move and check collision
            ball.move()
            ball.check_collision(paddle, block_manager.blocks, score_board)

            # draw game interface
            screen.fill(BLACK)
            # draw blocks manually
            for block in block_manager.blocks:
                screen.blit(block.image, block.rect)
            all_sprites.draw(screen)

            pygame.display.flip()
            clock.tick(60)

            if score_board.lives == 0:
                game_over = True

        else:
            if not show_game_over():
                running = False
            else:
                game_over = False
                block_manager.create_blocks()
                ball.reset()
                paddle.reset()
                score_board.reset()


# 运行游戏
if __name__ == "__main__":
    play_game()
