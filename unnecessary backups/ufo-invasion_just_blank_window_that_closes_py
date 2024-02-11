#  10 Feb 2024
# I'm try to re-make the alien invasion game from the book "python crash course"
# but re-factored and rotated 90 degrees to horizontal
# I also want to add some features like sound effects/music and maybe
# multiple stages (some of which are verticale), multiple keybindings for controls (if not custom keybindings)
# and mutliple enemy types
# first step: just get the player ship up on a screen

import sys, pygame
#from time import sleep # added page 272
from settings import Settings # i just copy/pasted from existing settings file (last version from chapter 14). i'll go back later and adjust if necessary
#from game_stats import GameStats
#from ship import Ship
#from bullet import Bullet
#from alien import Alien # modification for chapter 13 - bringing in the alien.py stuff
#from button import Button
#from scoreboard import Scoreboard

class UFOInvasion: 
    # Overall class to manage game assets and behavior 
    def __init__(self):
        ''' Initialize the game, and create game resources'''
################# boiler plate stuff ############################
        pygame.init()
        
        self.clock = pygame.time.Clock() # related to consistent frame rate - see also tick method
        self.settings = Settings() # yes, need settings file
        
        self.screen = pygame.display.set_mode(
            (
            self.settings.screen_width, 
            self.settings.screen_height
            )
        )
        pygame.display.set_caption("UFO Invasion")
################# boiler plate stuff ############################

# some variables for later. I'll uncomment as necessary

        # not anything to do yet but groups established
        self.bullets = pygame.sprite.Group() # create a group that holds the bullets 
        self.aliens = pygame.sprite.Group() # brought in for chapter 13 for the alien stuff

        # save these two for way later
        # self._create_fleet() 
        # self.play_button = Button(self, "Play")
        
            # per the book, methods that start with a _ are "helper methods"
    def run_game(self):    
        """start the main loop for the game"""
        while True:
            # have to go early stages to incrementally add
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() # don't forget paranse in that exist method! i think i forgot that the first time as well

            # about the only thing left without the other files existing - seems like part of boiler plate really
            pygame.display.flip()
            self.clock.tick(60) # related to consistent framerate - see also the self.clock line in the init function
            # Watch for keyboard and mouse events.
        
        
if __name__ == '__main__':
    
    # Make a game instance, and run the game
    # original used ai for instance name
    #so i was going to use 'ui' for 'ufo invastion' but apparently
    # 'ui' is already taken as a built-in class or whatever
    # so ufo inv it is then
    # also, the file isn't named 'main.py' which i thought was the purpose of this 
    # if __name__ - '__main__" thing but whatever, if it works it works
    ufoinv = UFOInvasion()
    ufoinv.run_game()