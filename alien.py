import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class which controls an individual alien"""

    def __init__(self, ai_settings, screen):
        """create an alien object"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the picture
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #create an alien at (0,0) and then set the correct location
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #save float number
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the alien"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """move the alien to left or right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """if the alien fleet touches the edge of the screen, return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True