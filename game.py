import pygame
import random
import time

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
background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

trash_img = pygame.image.load("trash.png")
trash_width, trash_height = 50, 50
trash_img = pygame.transform.scale(trash_img, (trash_width, trash_height))

clean_img = pygame.image.load("clean.jpeg")
clean_img = pygame.transform.scale(clean_img, (50, 50))

player_img = pygame.image.load("player.png")
player_width, player_height = 200, 200  # Increased player size
player_img = pygame.transform.scale(player_img, (player_width, player_height))

# Player attributes
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - player_height - 20
player_speed = 4  # Decreased player speed

# Trash attributes
trash_x = random.randint(0, WIDTH - trash_width)
trash_y = random.randint(50, max(50, HEIGHT - trash_height - 50))
trash_speed = 1.3  # Increased trash speed

# Score and missed trash count
score = 0
missed_trash = 0
font = pygame.font.Font(None, 36)

# Define instructions font
instructions_font = pygame.font.Font(None, 24)  # Use default font provided by pygame

# Display game name
intro_text = font.render("Today, recycle for a better tomorrow!", True, BLACK)
text_x = (WIDTH - intro_text.get_width()) // 2
text_y = HEIGHT // 4

# Display game over text
game_over_text = font.render("Game Over!", True, BLACK)
game_over_x = (WIDTH - game_over_text.get_width()) // 2
game_over_y = (HEIGHT - game_over_text.get_height()) // 2

# Define game instructions
instruction_text = instructions_font.render("Press any key to start!", True, BLACK)
instruction_x = (WIDTH - instruction_text.get_width()) // 2
instruction_y = HEIGHT // 2

# Define final message font
final_message_font = pygame.font.Font(None, 72)

# Final message text
final_message_text = final_message_font.render("Save your environment!", True, WHITE)
final_message_x = (WIDTH - final_message_text.get_width()) // 2
final_message_y = (HEIGHT - final_message_text.get_height()) // 2

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
        screen.blit(instruction_text, (instruction_x, instruction_y))

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
            missed_trash += 1  # Increase missed trash count

        # If missed trash reaches five, end the game
        if missed_trash >= 5:
            running = False

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

        # Display missed trash count
        missed_text = font.render(f"Missed: {missed_trash}/5", True, BLACK)
        screen.blit(missed_text, (10, 50))

    if not running:
        # Display game over text
        screen.blit(game_over_text, (game_over_x, game_over_y))
        pygame.display.update()
        # Pause for 3 seconds
        time.sleep(3)
        # Display final message
        screen.fill(BLACK)
        screen.blit(final_message_text, (final_message_x, final_message_y))
        pygame.display.update()
        # Pause for 3 seconds before quitting
        time.sleep(3)
        running = False

    # Update the display
    pygame.display.update()

pygame.quit()
