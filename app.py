import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Adventure")

# Fonts
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 24)

# Game levels data
levels = [
    {"name": "Level 1: Basic Syntax and Variables", "content": "Learn about variables and basic syntax."},
    {"name": "Level 2: Control Structures", "content": "Learn about if-else statements."},
    # Add more levels as needed
]

current_level = 0

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def game_loop():
    global current_level
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Display current level
        level = levels[current_level]
        draw_text(level["name"], font, BLACK, screen, 20, 20)
        draw_text(level["content"], small_font, BLACK, screen, 20, 80)

        # Update the display
        pygame.display.flip()
        clock.tick(60)

def level_one():
    level_text = "Level 1: Basic Syntax and Variables"
    tutorial_text = "Tutorial: Variables store information. Example: x = 5"
    challenge_text = "Challenge: Create a variable 'y' and assign it the value 10."

    code_input = ""

    clock = pygame.time.Clock()
    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Check the code input
                    if code_input.strip() == "y = 10":
                        return True  # Proceed to the next level
                    else:
                        code_input = ""  # Reset input
                elif event.key == pygame.K_BACKSPACE:
                    code_input = code_input[:-1]
                else:
                    code_input += event.unicode

        draw_text(level_text, font, BLACK, screen, 20, 20)
        draw_text(tutorial_text, small_font, BLACK, screen, 20, 80)
        draw_text(challenge_text, small_font, BLACK, screen, 20, 140)
        draw_text("Your Code: " + code_input, small_font, BLACK, screen, 20, 200)

        pygame.display.flip()
        clock.tick(60)

# Update the game loop to handle levels
def game_loop():
    global current_level
    clock = pygame.time.Clock()

    while True:
        if current_level == 0:
            if level_one():
                current_level += 1
        else:
            level = levels[current_level]
            screen.fill(WHITE)
            draw_text(level["name"], font, BLACK, screen, 20, 20)
            draw_text(level["content"], small_font, BLACK, screen, 20, 80)
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)

if __name__ == "__main__":
    game_loop()



