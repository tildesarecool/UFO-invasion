# settings.py - settings for alien invasion script
class Settings:
    """a class to store all settings for alien invasion"""
    def __init__(self):
        """initialize game's settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # ship settings - i decided to speed this up - was 1.5
        self.ship_speed = 3.0 # this actually only accepts ints so adjustments were made to ship.py
        # bullet settings - horizontal rather than vertical bullets so swap numbers
        self.bullet_speed = 4.0
        self.bullet_width = 15 # was 3
        self.bullet_height = 3 # was 15
        self.bullet_color = (60, 60, 60) # 60, 60, 60 is "dark gray"
        self.bullets_allowed = 6 # arbitrarily limit number of bulets on screen at once (page 251)
        