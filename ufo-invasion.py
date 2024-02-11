#  10 Feb 2024
# I'm try to re-make the alien invasion game from the book "python crash course"
# but re-factored and rotated 90 degrees to horizontal
# I also want to add some features like sound effects/music and maybe
# multiple stages (some of which are verticale), multiple keybindings for controls (if not custom keybindings)
# and mutliple enemy types
# 1st step: just get the player ship up on a screen - completed
# 2nd step: moving ship up/down constrained by top and bottom of window - completed (pending also refactor)
# 3rd step: placing an alien on screen at opposite end of window
# 4th step: firing bullet across screen

import sys, pygame
#from time import sleep # added page 272
from settings import Settings # i just copy/pasted from existing settings file (last version from chapter 14). i'll go back later and adjust if necessary
#from game_stats import GameStats
from ship import Ship 
#from bullet import Bullet
#from alien import Alien # modification for chapter 13 - bringing in the alien.py stuff
#from button import Button
#from scoreboard import Scoreboard
#from game_events import GameEvents #  it was taking too long to figure this out so i'll come back to the idea

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
        
         # added this line once i had apparently finished the initial version of the Ship class/ship.py
         # also blitme() line below
        self.ship = Ship(self)
        
        # departure from book for keybinds
        # I just assumed I needed to pass it self, which is ufo invasion class
        # just following how ship was done
        #self.events = GameEvents(self) # i don't think this is necessary
################# boiler plate stuff ############################

# some variables for later. I'll uncomment as necessary

        # not anything to do yet but groups established
        self.bulletsGroup = pygame.sprite.Group() # create a group that holds the bullets - changed name to be more descriptive/less confusing
        self.aliensGroup = pygame.sprite.Group() # group to hold aliens in fleet - changed name to be more descriptive/less confusing
        
        #there's some early stuff or setting bg color in __init__(self) but that will end up in _update screen later (pg. 231)
        # so I'm skipping it for (i may have to set it if i can't see the ship over the default black bg)
        
        # save these two for way later
        # self._create_fleet() 
        # self.play_button = Button(self, "Play")
        
            # per the book, methods that start with a _ are "helper methods"
    def run_game(self):    
        """start the main loop for the game"""
        while True:
            # in book it's just 
            # self._check_events()
            # so here it's just the extra step of the instantiated GameEvents class above, events, 
            # then _check_events() - should work the same
            self._check_events()
            self.ship.update()
            
            
            '''
            # these lines moved to game_events.py and GameEvents class
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() # don't forget paranse in that exist method! i think i forgot that the first time as well
            '''
            # class this in run game. it'll be defined below
            self._update_screen()

            # added this blitme() method and above self.ship = Ship(self) instantiation at same time
            # this method should draw the ship
            # this is when i find out how important setting a specific background is...the ship showed up. 
            # i'll do the bg thing later
           # self.ship.blitme() # moved to update_screen
            # about the only thing left without the other files existing - seems like part of boiler plate really
            #pygame.display.flip()
            self.clock.tick(60) # related to consistent framerate - see also the self.clock line in the init function
            # Watch for keyboard and mouse events.
        
        # the next step is separating the sys.exit/quit functionality 
        # as well as eventually ship movement key events into the _check_events() method
        # but I'd like to separate that into another file
        # this will be a departure from the book but...here goes
        # I'll call it game_events.py
        
        # now i could put the _update_screen method into a separate file too, but instead 
        # i'll just leave in here

###################################

    def _check_events(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: # physically push a key down
                if event.key == pygame.K_UP: # predefined which keyboard key - the up arrow
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
            # pushing key down versus releasing key and setting correlating variable to true/false
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False # when key released stop moving ship upwards
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

                
# ################################################################ #
#    def _check_keydown_events(self, event):
#        '''respond to keypresses'''
#        if event.key == pygame.K_UP:
#            self.ship.moving_top = True
#        elif event.key == pygame.K_DOWN:
#            self.ship.moving_bottom = True
#        elif event.key == pygame.K_q:
#            sys.exit()
#        elif event.key == pygame.K_SPACE:
#            self._fire_bullet()
    
#    def _check_keyup_events(self, event):
#        """repsond to key releases"""
#        if event.key == pygame.K_UP:
#            self.ship.moving_top = False
#        elif event.key == pygame.K_DOWN:
#            self.ship.moving_bottom = False
            

###################################



    def _update_screen(self):
        """update images on screen and flip to the new screen"""        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
    
    
    '''
    # here's the final version for reference
        def _update_screen(self):
        """update images on screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color) # 230,230,230 = light gray
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen) # added in chapter 13 to put the alien up on screen (pg. 258)
        
        # draw the score information
        self.sb.show_score()
        
        # Make the most recently drawn screen visible
        # Draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()
            
        pygame.display.flip()



    '''
        
        
if __name__ == '__main__':
    
    # Make a game instance, and run the game
    # original used ai for instance name
    #so i was going to use 'ui' for 'ufo invastion' but apparently
    # 'ui' is already taken as a built-in class or whatever
    # so ufo inv it is then
    # also, the file isn't named 'main.py' which i thought was the purpose of this 
    # if __name__ - '__main__" thing but whatever, if it works it works
    ufoinv = UFOInvasion()
    #ufoinv.events
    ufoinv.run_game()