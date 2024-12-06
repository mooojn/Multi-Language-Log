import pygame
import random
import csv

# Initialize pygame
pygame.init()
# Sound
pygame.mixer.init()

# Load sound effects
# asteroid_hit_sound = pygame.mixer.Sound('sounds/asteroid_hit.mp3')
# player_hit_sound = pygame.mixer.Sound('sounds/player_hit.mp3')
# bullet_shot_sound = pygame.mixer.Sound('sounds/bullet_shot.mp3')

# # Load and play background music
# pygame.mixer.music.load('bg.m4a')  # Replace with your music file
# pygame.mixer.music.play(-1)  # Play in an infinite loop (-1)

# Game window dimensions
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 650

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")

# High score tracker
high_score_file = "high_score.csv"

# Load or initialize high score
try:
    with open(high_score_file, 'r') as file:
        content = file.read().strip()  # Read and remove any leading/trailing whitespace
        high_score = int(content) if content else 0  # Convert to integer if content exists
except FileNotFoundError:
    high_score = 0


# Load player and asteroid images
player_img = pygame.image.load('images/player.png')
asteroid_img = pygame.image.load('images/asteroid.png')

# Player properties
player_width = 64
player_height = 64
player_x = WINDOW_WIDTH // 2 - player_width // 2
player_y = WINDOW_HEIGHT - player_height - 10
player_speed = 3

# Bullet properties
bullet_width = 8
bullet_height = 24
bullet_speed = 10
bullets = []

# Asteroid properties
asteroid_width = 64
asteroid_height = 55
asteroid_speed = 0.7
asteroids = []

# Scoring
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y - bullet_height])
                # bullet_shot_sound.play()  # Play the bullet shot sound

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - player_width:
        player_x += player_speed

    # Move bullets
    for bullet in bullets:
        bullet[1] -= bullet_speed

    # Generate asteroids
    if random.randint(1, 100) < 3:
        asteroids.append([random.randint(0, WINDOW_WIDTH - asteroid_width), 0])

    # Move asteroids
    for asteroid in asteroids:
        asteroid[1] += asteroid_speed

    # Collision detection
    for bullet in bullets:
        for asteroid in asteroids:
            if pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height).colliderect(
                    pygame.Rect(asteroid[0], asteroid[1], asteroid_width, asteroid_height)):
                bullets.remove(bullet)
                asteroids.remove(asteroid)
                # asteroid_hit_sound.play()  # Play the sound effect
                score += 1
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for asteroid in asteroids:
        asteroid_rect = pygame.Rect(asteroid[0], asteroid[1], asteroid_width, asteroid_height)
        if player_rect.colliderect(asteroid_rect):
            if score > high_score:
                high_score = score
                with open(high_score_file, 'w') as file:
                    file.write(str(high_score))
            score = 0
            # player_hit_sound.play()  # Play the player hit sound
            asteroids = []  # Reset asteroids
            break
    
    # Clear the screen
    window.fill(BLACK)

    # Draw player
    window.blit(player_img, (player_x, player_y))

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(window, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))

    # Draw asteroids
    for asteroid in asteroids:
        window.blit(asteroid_img, (asteroid[0], asteroid[1]))

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    window.blit(score_text, (10, 10))

    # Draw high score
    high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
    window.blit(high_score_text, (10, 40))  # Adjust the position as needed

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
