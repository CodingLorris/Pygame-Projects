import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 2 * player_size
player_speed = 7
jump_count = 10
is_jumping = False

# Platforms
platform_width = 100
platform_height = 20
platforms = [
    (150, HEIGHT - 100),
    (350, HEIGHT - 200),
    (550, HEIGHT - 300),
]

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario-like Platformer")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    # Jumping
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    # Gravity
    if player_y < HEIGHT - player_size:
        player_y += 5

    # Check for collisions with platforms
    for platform in platforms:
        if (
            platform[0] < player_x + player_size
            and platform[0] + platform_width > player_x
            and platform[1] < player_y + player_size
            and platform[1] + platform_height > player_y
        ):
            player_y = platform[1] - player_size

    # Clear the screen
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, RED, [player_x, player_y, player_size, player_size])

    # Draw the platforms
    for platform in platforms:
        pygame.draw.rect(screen, RED, [platform[0], platform[1], platform_width, platform_height])

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(FPS)
