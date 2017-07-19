import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

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
        gf.check_events()

        gf.update_screen(ai_settings,screen,ship)

run_game()

