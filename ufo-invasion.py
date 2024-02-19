#  10 Feb 2024
# I'm try to re-make the alien invasion game from the book "python crash course"
# but re-factored and rotated 90 degrees to horizontal
# I also want to add some features like sound effects/music and maybe
# multiple stages (some of which are verticale), multiple keybindings for controls (if not custom keybindings)
# and mutliple enemy types
# - 1st step: just get the player ship up on a screen - completed
# - 2nd step: moving ship up/down constrained by top and bottom of window - completed 
#  - 3rd step: firing bullet across screen - completed (bullets don't delete themselves yet)
#  - 4th step: placing 1 column of aliens on screen at opposite end of window via while loop - (alies show up, while loop pending)
#  - 5th step: draw multiple columns of aliens via embedded while loops
#  - 6th step: bullets collid with aliens, elminating each one
#  - 7th step: scoring system, tracking number of tries/game restarts left
#  - 8th step: a "click to play" button/pause button

# Stretch/dream/at the end goals:
# - music, sound effects
# - save settings to JSON file/load settings from JSON file
#   - a settings menu in-game where things like sound volume and resolution could be set
#   - a "secret" debug input box i can access to change setting values while playing
# - at least two different varieties of enemies
#   - one or all enemies fly in patterns instead of move down/move up/move closer
#   - enemies fire bullets back at random


import sys, pygame, os
#from time import sleep # added page 272
from settings import Settings # i just copy/pasted from existing settings file (last version from chapter 14). i'll go back later and adjust if necessary
#from game_stats import GameStats
from ship import Ship 
from bullet import Bullet
from alien import Alien # modification for chapter 13 - bringing in the alien.py stuff
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
        
        
        ##### I added this related to the additional save/load settings in settings.py
        ##### which I got from chatgpt - 15 feb 2024
        if not os.path.exists("settings.json"):
            try:
                self.settings.save_settings_to_json("settings.json")
            except Exception as e:
                print(f"Error saving settings file - error is: {e}")
        else:
            self.settings.load_settings_from_json("settings.json")
        
        ##### I added this related to the additional save/load settings in settings.py
        ##### which I got from chatgpt - 15 feb 2024
        
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
        self._create_fleet() 
        # self.play_button = Button(self, "Play")
        
            # per the book, methods that start with a _ are "helper methods"
        
        
        
# This is the code for full screen, which looks terrible on my giant monitor - 
# page 245 - after implementing it the books says (paraphrasing)
# "but if that doesn't work good that keep the old code" - could have said that first!
#        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#        self.settings.screen_width = self.screen.get_rect().width
#        self.settings.screen_height = self.screen.get_rect().height

    def run_game(self):    
        """start the main loop for the game"""
        while True:
            # in book it's just 
            # self._check_events()
            # so here it's just the extra step of the instantiated GameEvents class above, events, 
            # then _check_events() - should work the same
            self._check_events()
            self.ship.update()
            #self.bullet.update()
            self.bulletsGroup.update() # I renamed the bullet group from "bullets" to "bulletsGroup"
            
            
            
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
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


                
# ################################################################ #
    def _check_keydown_events(self, event):
        '''respond to keypresses'''
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        #elif event.key == pygame.K_SPACE:
        #    self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """repsond to key releases"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            
    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group"""
        # arbitrarily limit number of bullets on screen at once (page 251) see also bullets.py
        # the first version of this after that max bullets no bullets at all fire
        if len(self.bulletsGroup) < self.settings.bullets_allowed: 
            new_bullet = Bullet(self)
            self.bulletsGroup.add(new_bullet) # new bullet group name hits me again. only took a few minutes to find though
            
###################################


    def _create_fleet(self):  # brought in for chapter 13 for the alien stuff - called above rungame method
        """create the fleet of aliens"""
        # create an alien and keep adding aliens until there's no room left
        # spacing between aliens is one alien width and one alien height
        # make an alien
        # in my experimenting i was skipping some steps for troubleshooting -
        # i wanted to just added lots of aliens and skip the while loop to show just one at a time
        # but also skipped adding aliens to alienGroup
        # and the _update_screen only writes that group to the screen so once i added the aliens to the group 
        # magically they showed up. now just have to add one a time maybe
        # these two lines
        # self.aliensGroup.add(alien)
        # self.aliensGroup.add(new_alien)
        alien = Alien(self) # just creating first alien at that original position defined in alien.py
        alien_height = alien.rect.height # just the height of the alien so we have it for later
        alien_width = alien.rect.width # alien.rect.width was used below for xpos anyway. i guess this just shortens it slightly
        #alien_fleet_spacing = alien.rect.height * 2
        # I rcreated the self.settings.fleet_ship_spacing as a variable in settings.py
        # so i could easily adjust it like everything else - note: 10px might be too much
        self.screen_rect = self.screen.get_rect() # make rectangle out of dimensions of window
        # these two lines create an initial x location: 
        # (window width - 1200) - (width of alien rectangle, 58) - 20 = 1122 - if my numbers are right - 78px in from right
        # I'm not sure xpos is even needed. just seems like too many variables to track
        #alien.xpos = self.screen_rect.width - alien_width - 20
        # the x of the alien rectangle is equal to the result of the xpos calculation
        alien.rect.x = float(self.screen_rect.width - alien_width - 20) 
        alien.x = alien.rect.x 
        # now i'll do the height/y side of it
        # the alien is as far down from the top of the window as the alien image is high
        # since the alien is 58 pixels high, it'd be 58px down from the top
        # setting rectangle first
        alien.rect.y = alien.rect.height
        # so the alien y coord is now the same as the y coord of the alien rectangle
        alien.y = float(alien.rect.y) 
        print(f"alien.y is now {alien.y} ")
        print(f"alien.x is {alien.x}")
        # for this first column x will be the same for all of them, it's only y that has to be 
        # re-calculated
# so the x of the alien should be 78px in from the right side of the screen
# and the y of the alien as of now at least should be an height's worth of pixels down from the top of screen
        # so current y takes that y position and implents that ship space
        # although maybe that should be a plus?
        current_y = alien.y - self.settings.fleet_ship_spacing 
        current_x = alien.x
        print(f"current_y is {current_y} ")
        # this "debugging" while loop did produce the 4 aliens for the fleet, i can swap back other one 
        #i = 1
        #while i <= 9:
        print(f"alien_height is now {alien_height} ")
        print(f"current_y is {current_y} and self.settings.screen_height - (alien_height * 2)   is now {self.settings.screen_height - (alien_height * 2)  } ")
        # this should be the good while loop. changing it briefly for troubleshooting
        #      current y starts at 38 -  should be 800     height is 58 * 2 = 116 eg 800 - 116 = 644
        print(f"alien.x - (alien_width * 3) is {alien.x - (alien_width * 3)}")
        print(f"current_x is {current_x} ")
        print(f"alien.x is {alien.x} ")
        #breakpoint()
#        while current_x < (self.settings.screen_width - (alien_width * 3) ):  # current_x defined above: float(self.screen_rect.width - alien_width - 20) 
        while current_x <= alien.x - (alien_width * 3):
            #pass
            while current_y < ( self.settings.screen_height - (alien_height * 2)  ):
                # switching over to using _create_alien() method
                #self._create_alien(current_y)
                #my_alien = self._create_alien(self.settings.screen_height - (alien_height * 2))
                #   first time through loop sending 38 to create alien method (as float)
                my_alien = self._create_alien(current_y, current_x)
                print(f"my_alien[0] is {my_alien[0]} and my_alien[1] is {my_alien[1]}")
#print(f"my_alien[0] is {my_alien[0]}")
                #print(f"my_alien.y is {my_alien.y}")
                #my_alien.y
    # now i'll re-assign current_y to value of the prior alien (subtract ship spacing)
    # I've implmented this differently: create_alien returns it's rect.bottom 
    # so this "should" spawn a new alien each time through the loop make current_y (add that alien bottom + ship spacing)
    # and send that new current_y back into the create_ alien to repeat once more
    # issue is apparently it's not retain the alien x each time through the loop so the x is upper right corner (or something?)
    # - i ended up just making create_alien take in both x and y and defining x to send in to the create_alien
    # this appears to have worked for alien one once again, now i'd like to produce 3 or 4 aliens as I did previously with
    # the while loop before swapping back to conditions based on screen height nevermind adding in additional columns
                current_y = my_alien[0] + self.settings.fleet_ship_spacing # inner while
            
            
                
            current_y = alien.y - self.settings.fleet_ship_spacing  # outer while
            current_x = my_alien[1] - self.settings.fleet_ship_spacing  
            
# print(f"current_y with adding my alien and ship spacing is is now {current_y} ")
                #breakpoint()
                #print(f"self.settings.screen_heightis {self.settings.screen_height} ")
                # third_alien.rect.y = sec_alien.rect.bottom + self.settings.fleet_ship_spacing 
                #i += 1
                #break

    def _create_alien(self, current_y, current_x):
        """ Create an alien and place it in the row """
        fleet_alien = Alien(self)
        fleet_alien.y = current_y
        print(f"current_y of fleet_alien is {fleet_alien.y}")
        #fleet_alien.rect.
        #alien.rect.y = alien.rect.height
        fleet_alien.rect.y = current_y
        print(f"fleet_alien.rect.y is {fleet_alien.rect.y}")
        
        fleet_alien.rect.x = current_x
        fleet_alien.x = current_x
        
        #breakpoint()
        self.aliensGroup.add(fleet_alien)
        # could I just return the fleet alien itself? so I can access the bottom and left sides
        # from other loop? or just return fleet_alien.rect?
        #fleet_alien.rect
        return fleet_alien.rect.bottom, fleet_alien.rect.left

    def _update_screen(self):
        """update images on screen and flip to the new screen"""        
        self.screen.fill(self.settings.bg_color)
        
        for bullet in self.bulletsGroup.sprites():
            bullet.draw_bullet()
        
        self.ship.blitme()
        self.aliensGroup.draw(self.screen) # draw is alien group method
        pygame.display.flip()

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