#  10 Feb 2024
# I'm try to re-make the alien invasion game from the book "python crash course"
# but re-factored and rotated 90 degrees to horizontal
# I also want to add some features like sound effects/music and maybe
# multiple stages (some of which are verticale), multiple keybindings for controls (if not custom keybindings)
# and mutliple enemy types
# first step: just get the player ship up on a screen

import sys, pygame
#from time import sleep # added page 272
#from settings import Settings
#from game_stats import GameStats
#from ship import Ship
#from bullet import Bullet
#from alien import Alien # modification for chapter 13 - bringing in the alien.py stuff
#from button import Button
#from scoreboard import Scoreboard

class UFOInvasion: 
    # Overall class to manage game assets and behavior 
    def __init__(self):
################# boiler plate stuff ############################
        pygame.init()
        self.clock = pygame.time.Clock() # related to consistent frame rate - see also tick method
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (
            self.settings.screen_width, 
            self.settings.screen_height
            )
        )
################# boiler plate stuff ############################