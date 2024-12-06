import pygame
import random

# Initialize pygame
pygame.init()

# Game window dimensions
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Ball properties
ball_radius = 20
ball_speed_x = 0.5
ball_speed_y = 0.5
ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2

# Paddle properties
paddle_width = 15
paddle_height = 100
paddle_speed = 1
left_paddle_x = 50
left_paddle_y = WINDOW_HEIGHT // 2 - paddle_height // 2
right_paddle_x = WINDOW_WIDTH - 50 - paddle_width
right_paddle_y = WINDOW_HEIGHT // 2 - paddle_height // 2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < WINDOW_HEIGHT - paddle_height:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < WINDOW_HEIGHT - paddle_height:
        right_paddle_y += paddle_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom edges
    if ball_y <= 0 or ball_y >= WINDOW_HEIGHT - ball_radius:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if left_paddle_y <= ball_y <= left_paddle_y + paddle_height and ball_x - ball_radius <= left_paddle_x + paddle_width:
        ball_speed_x = -ball_speed_x
    if right_paddle_y <= ball_y <= right_paddle_y + paddle_height and ball_x + ball_radius >= right_paddle_x:
        ball_speed_x = -ball_speed_x

    # Ball out of bounds
    if ball_x <= 0 or ball_x >= WINDOW_WIDTH:
        ball_x = WINDOW_WIDTH // 2
        ball_y = WINDOW_HEIGHT // 2
        ball_speed_x = random.choice([-0.7, 0.7])
        ball_speed_y = random.choice([-0.7, 0.7])

    # Clear the screen
    window.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(window, WHITE, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(window, WHITE, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(window, WHITE, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
