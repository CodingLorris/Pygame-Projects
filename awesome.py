import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Awesome Space Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5

# Enemy
enemy_size = 50
enemy_speed = 3
enemies = []

# Clock to control the frame rate
clock = pygame.time.Clock()

# Score
score = 0

# Fonts
font = pygame.font.SysFont(None, 40)

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(screen, white, [x, y, player_size, player_size])

# Function to draw an enemy
def draw_enemy(x, y):
    pygame.draw.rect(screen, red, [x, y, enemy_size, enemy_size])

# Function to display the score
def show_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    # Boundaries for the player
    if player_x < 0:
        player_x = 0
    elif player_x > width - player_size:
        player_x = width - player_size

    # Update enemies
    for enemy in enemies:
        enemy[1] += enemy_speed
        if enemy[1] > height:
            enemies.remove(enemy)
            score += 1

    # Add new enemies
    if random.randint(0, 100) < 5:
        enemy_x = random.randint(0, width - enemy_size)
        enemy_y = -enemy_size
        enemies.append([enemy_x, enemy_y])

    # Check for collisions
    for enemy in enemies:
        if (
            player_x < enemy[0] + enemy_size
            and player_x + player_size > enemy[0]
            and player_y < enemy[1] + enemy_size
            and player_y + player_size > enemy[1]
        ):
            game_over = True

    # Clear the screen
    screen.fill(black)

    # Draw the player and enemies
    draw_player(player_x, player_y)
    for enemy in enemies:
        draw_enemy(enemy[0], enemy[1])

    # Display the score
    show_score(score)

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
