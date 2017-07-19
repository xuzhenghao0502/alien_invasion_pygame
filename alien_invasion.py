import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    #initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #create a ship
    ship = Ship(screen)

    #set background color
    bg_color = (230,230,230)

    #the main loop of the game
    while True:
        #monitor the keyboard and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #redraw the screen
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #visualize the display
        pygame.display.flip()

run_game()

