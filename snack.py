import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
blue = (255, 255, 0)
white = (255, 255, 255)
red = (255, 255, 255)
score_color = (255, 255, 0)

# Snake initial position and size
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = (1, 0)

# Food initial position
food = (300, 200)

# Score
score = 0

# Game loop
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, 1):
        snake_direction = (0, -1)
    elif keys[pygame.K_DOWN] and snake_direction != (0, -1):
        snake_direction = (0, 1)
    elif keys[pygame.K_LEFT] and snake_direction != (1, 0):
        snake_direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
        snake_direction = (1, 0)

    # Move the snake
    x, y = snake[0]
    x += snake_direction[0] * 10
    y += snake_direction[1] * 10
    snake.insert(0, (x, y))

    # Check for collisions with food
    if (
        food[0] <= x <= food[0] + 10
        and food[1] <= y <= food[1] + 10
    ):
        food = (random.randint(0, width - 10), random.randint(0, height - 10))
        score += 1
    else:
        snake.pop()

    # Check for collisions with walls or itself
    if (
        x < 0
        or x >= width
        or y < 0
        or y >= height
        or any(segment == (x, y) for segment in snake[1:])
    ):
        game_over_text = font.render("Game Over", True, red)
        screen.blit(game_over_text, (width // 2 - 100, height // 2 - 18))
        pygame.display.flip()
        pygame.time.delay(2000)  # Pause for 2 seconds
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, red, (*food, 10, 10))
    for segment in snake:
        pygame.draw.rect(screen, blue, (*segment, 10, 10))

    # Display score
    score_text = font.render(f"Score: {score}", True, score_color)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Control the game speed
    clock.tick(15)
