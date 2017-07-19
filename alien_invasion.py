import sys

import pygame

def run_game():
    #initialize the game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    #set background color
    bg_color = (230,230,230)

    #the main loop of the game
    while True:
        #monitor the keyboard and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #redraw the screen
        screen.fill(bg_color)

        #visualize the display
        pygame.display.flip()

run_game()

