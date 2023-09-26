import pygame
from pong import Pong
from ai_player import AIPlayer
# Initialize pygame
pygame.init()
# Set up the screen
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("AI Pong Game")
# Create the pong objects
left_pong = Pong(screen, screen_width, screen_height, "left")
right_pong = Pong(screen, screen_width, screen_height, "right")
# Create the AI players
left_ai_player = AIPlayer(left_pong, screen_height)
right_ai_player = AIPlayer(right_pong, screen_height)
# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update the pong objects
    left_pong.update()
    right_pong.update()
    # Update the AI players
    left_ai_player.update()
    right_ai_player.update()
    # Clear the screen
    screen.fill((0, 0, 0))
    # Draw the pong objects
    left_pong.draw()
    right_pong.draw()
    # Update the display
    pygame.display.flip()
    # Set the frame rate
    clock.tick(60)
# Quit the game
pygame.quit()