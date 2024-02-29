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
BLACK = (0, 0, 0)

# Load and resize images
background_img = pygame.image.load("background.jpeg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

trash_img = pygame.image.load("trash.jpg")
trash_width, trash_height = 50, 50
trash_img = pygame.transform.scale(trash_img, (trash_width, trash_height))

clean_img = pygame.image.load("clean.jpeg")
clean_img = pygame.transform.scale(clean_img, (50, 50))

player_img = pygame.image.load("player.jpeg")
player_width, player_height = 100, 100  # Increased player size
player_img = pygame.transform.scale(player_img, (player_width, player_height))

# Player attributes
player_x = (WIDTH - player_width) // 2  # Center player horizontally
player_y = HEIGHT - player_height - 20
player_speed = 8  # Increased player speed

# Trash attributes
trash_x = random.randint(0, WIDTH - trash_width)
trash_y = random.randint(50, max(50, HEIGHT - trash_height - 50))
trash_speed = 1  # Decreased trash speed significantly

# Score
score = 0
font = pygame.font.Font(None, 36)

# Define instructions font
instructions_font = pygame.font.Font("freesansbold.ttf", 24)

# Display game name
intro_text = font.render("Clean Up the Environment!", True, BLACK)
text_x = (WIDTH - intro_text.get_width()) // 2
text_y = HEIGHT // 4

# Display game instructions
instruction_text1 = instructions_font.render("Press any key to start!", True, BLACK)
instruction_text2 = instructions_font.render("Use arrow keys to move and collect trash.", True, BLACK)
instruction_text3 = instructions_font.render("Avoid letting trash fall off the screen.", True, BLACK)
instruction_x = (WIDTH - instruction_text1.get_width()) // 2
instruction_y = HEIGHT // 2

# Game loop
game_started = False
running = True
while running:
    screen.fill(WHITE)
    screen.blit(background_img, (0, 0))

    # Display game name
    screen.blit(intro_text, (text_x, text_y))

    if not game_started:
        # Display game instructions
        screen.blit(instruction_text1, (instruction_x, instruction_y))
        screen.blit(instruction_text2, (instruction_x, instruction_y + 50))
        screen.blit(instruction_text3, (instruction_x, instruction_y + 100))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            game_started = True  # Start the game when any key is pressed

    if game_started:
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
