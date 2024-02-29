import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clean Up the Environment!")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Load images
background_img = pygame.image.load("background.jpeg")
trash_img = pygame.image.load("trash.jpg")
clean_img = pygame.image.load("clean.jpeg")
# Player attributes
player_img = pygame.image.load("player.png")
player_width, player_height = player_img.get_rect().size
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 20
player_speed = 5

# Trash attributes
trash_width, trash_height = trash_img.get_rect().size
trash_x = random.randint(0, WIDTH - trash_width)
trash_y = random.randint(50, HEIGHT - trash_height - 50)
trash_speed = 3

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    screen.blit(background_img, (0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Boundary check for player
    if player_x < 0:
        player_x = 0
    elif player_x > WIDTH - player_width:
        player_x = WIDTH - player_width

    # Move trash
    trash_y += trash_speed
    if trash_y > HEIGHT:
        trash_x = random.randint(0, WIDTH - trash_width)
        trash_y = -trash_height
        score -= 1

    # Collision detection
    if player_x < trash_x + trash_width and player_x + player_width > trash_x \
            and player_y < trash_y + trash_height and player_y + player_height > trash_y:
        trash_x = random.randint(0, WIDTH - trash_width)
        trash_y = -trash_height
        score += 1

    # Display trash and player
    screen.blit(trash_img, (trash_x, trash_y))
    screen.blit(player_img, (player_x, player_y))

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

pygame.quit()
