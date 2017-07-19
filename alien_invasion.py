import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
# from alien import Alien

def run_game():
    #initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #create a ship
    ship = Ship(ai_settings, screen)

    #create an alien
    # alien = Alien(ai_settings, screen)

    #create a group containing all the bullets
    bullets = Group()
    aliens = Group()

    #create a group of alien
    gf.create_fleet(ai_settings, screen, aliens)

    #set background color
    bg_color = (230,230,230)

    #the main loop of the game
    while True:
        #monitor the keyboard and mouse event
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship, aliens, bullets)

run_game()

