
import sys , pygame
from pygame.locals import *
from settings import Settings
from ship import Ship

def main():
    #Initialize game,settings and create a scren object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_widht,ai_settings.screen_height))

    # Make a  ship
    ship = Ship(screen)

    #Start the main loop fot the game
    while True:

        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == QUIT:
               sys.exit(0)
        # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    main()