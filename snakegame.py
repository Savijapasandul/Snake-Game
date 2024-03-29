import pygame
import random
from collections import deque

pygame.init()

# Constants
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
DIS_WIDTH = 600
DIS_HEIGHT = 400
SNAKE_BLOCK = 20  # Double the size of the original block
SNAKE_SPEED = 15
FONT_STYLE = pygame.font.SysFont("bahnschrift", 25)
SCORE_FONT = pygame.font.SysFont("comicsansms", 35)

# Load sound effects
eat_sound = pygame.mixer.Sound("src/eat.wav")
game_over_sound = pygame.mixer.Sound("src/game_over.wav")

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def add_wall():
    wall_x = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 20.0) * 20.0  # Adjusted for the doubled block size
    wall_y = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0  # Adjusted for the doubled block size
    return wall_x, wall_y

def game_loop():
    dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    snake = deque([(DIS_WIDTH / 2, DIS_HEIGHT / 2)])
    snake_dir = (0, 0)
    food_pos = (round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 20.0) * 20.0,  # Adjusted for the doubled block size
                round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0)  # Adjusted for the doubled block size
    score = 0
    walls = []

    game_over = False
    game_close = False

    while not game_over:
        while game_close:
            dis.fill(BLUE)
            draw_text("You Lost! Press C-Play Again or Q-Quit", FONT_STYLE, RED, dis, DIS_WIDTH / 6, DIS_HEIGHT / 3)
            draw_text("Your Score: " + str(score), SCORE_FONT, YELLOW, dis, 0, 0)
            pygame.display.update()

            game_over_sound.play()
            sound_start_time = pygame.time.get_ticks()  # Get the current time
            sound_duration = 1000  # 1 second in milliseconds
            while pygame.time.get_ticks() - sound_start_time < sound_duration:  # Play for 1 second
                # Calculate the elapsed time
                elapsed_time = pygame.time.get_ticks() - sound_start_time
                # Calculate the remaining time
                remaining_time = sound_duration - elapsed_time
                # Calculate the volume factor based on the remaining time
                volume_factor = remaining_time / sound_duration
                # Set the volume of the sound
                game_over_sound.set_volume(volume_factor)
                pygame.time.delay(5000)  # Adjust this delay as needed to control the speed of volume reduction

            game_over_sound.stop()  # Stop the sound

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                elif event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and snake_dir != (SNAKE_BLOCK, 0):
                    snake_dir = (-SNAKE_BLOCK, 0)
                elif event.key == pygame.K_RIGHT and snake_dir != (-SNAKE_BLOCK, 0):
                    snake_dir = (SNAKE_BLOCK, 0)
                elif event.key == pygame.K_UP and snake_dir != (0, SNAKE_BLOCK):
                    snake_dir = (0, -SNAKE_BLOCK)
                elif event.key == pygame.K_DOWN and snake_dir != (0, -SNAKE_BLOCK):
                    snake_dir = (0, SNAKE_BLOCK)

        head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

        if head[0] >= DIS_WIDTH or head[0] < 0 or head[1] >= DIS_HEIGHT or head[1] < 0:
            game_close = True

        if head == food_pos:
            score += 1
            food_pos = (round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 20.0) * 20.0,  # Adjusted for the doubled block size
                        round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 20.0) * 20.0)  # Adjusted for the doubled block size
            if score > 5:
                walls.append(add_wall())
            eat_sound.play()  # Play eat sound
            sound_start_time = pygame.time.get_ticks()  # Get the current time
            while pygame.time.get_ticks() - sound_start_time < 1000:  # Play for 1 second
                pass
            eat_sound.stop()  # Stop the sound
        else:
            snake.pop()

        if head in snake or head in walls:
            game_close = True

        snake.appendleft(head)

        dis.fill(BLUE)
        pygame.draw.rect(dis, GREEN, (*food_pos, SNAKE_BLOCK, SNAKE_BLOCK))  # Adjusted for the doubled block size
        for pos in snake:
            pygame.draw.rect(dis, BLACK, (*pos, SNAKE_BLOCK, SNAKE_BLOCK))  # Adjusted for the doubled block size
        for wall in walls:
            pygame.draw.rect(dis, RED, (*wall, SNAKE_BLOCK, SNAKE_BLOCK))  # Adjusted for the doubled block size
        draw_text("Your Score: " + str(score), SCORE_FONT, YELLOW, dis, 0, 0)
        pygame.display.update()

        # Adjust snake speed based on score
        if score < 10:
            SNAKE_SPEED = 10
        elif score < 20:
            SNAKE_SPEED = 12
        elif score < 30:
            SNAKE_SPEED = 15
        else:
            SNAKE_SPEED = 10

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game_loop()
