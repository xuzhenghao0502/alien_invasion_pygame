class Settings():
    """save all the setting configuations here"""
    def __init__(self):
        """initialize the configuration in the game"""
        #set the screen
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #set the ship speed
        self.ship_speed_factor = 1.5

        #set the bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
