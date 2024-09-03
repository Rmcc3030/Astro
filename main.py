import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
    while True:
        # Add code to handle events, such as checking if the window is closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Your additional code should be added here, at the beginning of each loop iteration
        # For example, you might check for specific key presses, update timers, etc.
        # Example: Print "Loop iteration started" to demonstrate adding code here
        print("Loop iteration started")

        # Clear the screen with a solid black color
        screen.fill((0, 0, 0))  # Fill the screen with black

        # Refresh the screen to update the display
        pygame.display.flip()  # Refresh the screen

if __name__ == "__main__":
    main()
