import sys

import pygame

def check_events():
    # monitor the keyboard and mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """update the images on the screen and tab to the new screen"""
    # redraw the screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # visualize the display
    pygame.display.flip()
