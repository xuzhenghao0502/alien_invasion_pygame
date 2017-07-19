import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """initialize the ship and its location"""
        self.screen = screen
        self.ai_settings = ai_settings

        #load the ship image and get its outer frame
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #movement flag
        self.moving_right = False
        self.moving_left = False

        #put all the new ship on the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #save float number into the ship.center
        self.center = float(self.rect.centerx)

    def blitme(self):
        """draw the ship at a certain location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update the location of ship based on the movement flag"""
        #update float(center) instead of int(rect.centerx)
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left == True and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #update self.rect.centerx based on center
        self.rect.centerx = self.center