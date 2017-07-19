import pygame

class Ship():
    def __init__(self,screen):
        """initialize the ship and its location"""
        self.screen = screen

        #load the ship image and get its outer frame
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put all the new ship on the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """draw the ship at a certain location"""
        self.screen.blit(self.image, self.rect)