
import sys , pygame
from pygame.locals import *

def main():
    #Initialize game and create a scren object.
    pygame.init()
    screen = pygame.display.set_mode((1200,800))

    # Set the background color.
    bg_color = (230,230,230)

    #Start the main loop fot the game
    while True:

        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == QUIT:
               sys.exit(0)
        # Redraw the screen during each pass through the loop
        screen.fill(bg_color)

        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    main()