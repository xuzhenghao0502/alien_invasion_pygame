import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class which control the configurations for all bullets"""

    def __init__(self, ai_settings, screen, ship):
        """create a bullet object at the ship"""
        super(Bullet,self).__init__()
        self.screen = screen

        #create a bullet at (0,0), then set the correct position
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move the bullet from bottom to top"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)