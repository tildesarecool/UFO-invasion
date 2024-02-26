#  10 Feb 2024
# I'm try to re-make the alien invasion game from the book "python crash course"
# but re-factored and rotated 90 degrees to horizontal
# I also want to add some features like sound effects/music and maybe
# multiple stages (some of which are verticale), multiple keybindings for controls (if not custom keybindings)
# and mutliple enemy types
# - 1st step: just get the player ship up on a screen - completed
# - 2nd step: moving ship up/down constrained by top and bottom of window - completed 
#  - 3rd step: firing bullet across screen - completed 
#  - 4th step: placing 1 column of aliens on screen at opposite end of window via while loop - completed
#  - 5th step: draw multiple columns of aliens via embedded while loops - completed
#  - 6th step: bullets collid with aliens, elminating each one - completed
#  - 7th step: scoring system, tracking number of tries/game restarts left - completed
#  - 8th step: a "click to play" button/pause button (end of game, no pause yet - partially completed)

# Stretch/dream/at the end goals:
# - music, sound effects
# - save settings to JSON file/load settings from JSON file
#   - a settings menu in-game where things like sound volume and resolution could be set
#   - a "secret" debug input box i can access to change setting values while playing
# - at least two different varieties of enemies
#   - one or all enemies fly in patterns instead of move down/move up/move closer
#   - enemies fire bullets back at random


import sys, pygame, os
from time import sleep # added page 272
from settings import Settings # i just copy/pasted from existing settings file (last version from chapter 14). i'll go back later and adjust if necessary
from game_stats import GameStats
from ship import Ship 
from bullet import Bullet
from alien import Alien # modification for chapter 13 - bringing in the alien.py stuff
from button import Button
from scoreboard import Scoreboard

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
        
        self.stats = GameStats(self) # added page 272
        self.sb = Scoreboard(self)
        

        self.ship = Ship(self)
        

################# boiler plate stuff ############################

        self.bulletsGroup = pygame.sprite.Group() # create a group that holds the bullets - changed name to be more descriptive/less confusing
        self.aliensGroup = pygame.sprite.Group() # group to hold aliens in fleet - changed name to be more descriptive/less confusing
                
        self._create_fleet() 
        
        self.game_active = False # this can be used for a pause menu. probably.
        
        # make the play button
        self.play_button = Button(self, "Play")
        

        
# This is the code for full screen, which looks terrible on my giant monitor - 
# page 245 - after implementing it the books says (paraphrasing)
# "but if that doesn't work good then keep the old code" - could have said that first!
#        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#        self.settings.screen_width = self.screen.get_rect().width
#        self.settings.screen_height = self.screen.get_rect().height

    def run_game(self):    
        """start the main loop for the game"""
        while True:

            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets() 
                self._update_aliens()

            self.bulletsGroup.update() # I renamed the bullet group from "bullets" to "bulletsGroup"
            self._update_screen()
            self.clock.tick(60) # related to consistent framerate - see also the self.clock line in the init function

###################################

    def _check_events(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: # physically push a key down
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)



    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings()
            
            self.stats.reset_stats()
            self.sb.prep_score() # added pg 289
            self.sb.prep_level() # added pg. 295
            self.sb.prep_ships() # from pg. 298
            self.game_active = True
            # get rid of any remaining bullets and alines
            self.bulletsGroup.empty()
            self.aliensGroup.empty()
            
            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            
            #Hide the mouse cursor
            pygame.mouse.set_visible(False)

                
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
            self.bulletsGroup.add(new_bullet) 
            print(f"bulletgroup length is now {len(self.bulletsGroup)} (firebullet method)")

    def _update_bullets(self):
        """update position of bullets and get rid of old bullets"""
        # update bullet position
        self.bulletsGroup.update() # changed from "bullets" to "bulletsGroup"
        # get rid of bullets that have disappeared - re-adjusted for right side instead of bottom
        for bullet in self.bulletsGroup.copy(): # changed from "bullets" to "bulletsGroup"

            if bullet.rect.right >= self.screen_rect.right:
                self.bulletsGroup.remove(bullet) # changed from "bullets" to "bulletsGroup"
                print(f"bulletgroup length is now {len(self.bulletsGroup)} (update bullets method)")

        self._check_bullet_alien_collisions()




    def _check_bullet_alien_collisions(self): 
        """respond to bullet-alien collisions"""
        #remove any bullets and aliens that have colided
        collisions = pygame.sprite.groupcollide( 
                        self.bulletsGroup, 
                        self.aliensGroup, 
                        False, # when this is false bullets pass through aliens and keep going
                        True 
                        ) # added as part of bullets/collision, pg. 267
        # per the book:
        # for a high powered bullet that can travel to the top of screen/destroy all enemies it encounters, set the first boolean to false
        # and keep the second boolean true.  would make that bullet active until it reached the top of the screen
        if collisions: # if the collisions dictionary even exists
            for aliens in collisions.values(): # go through the values in the dictionary
                # add score by points aliens are worth times how big that alien value is
                # also, this 'aliens' from for loop so...not group then
                self.stats.score += self.settings.alien_points * len(aliens) 
            self.sb.prep_score()
            self.sb.check_high_score() # added in association with high score updates in scoreboard.py - pg. 293

        # part of spawning new fleet once fleet destroyed - pg. 268     
        if not self.aliensGroup:
            # destroy existing bullets and create new fleet
            self.bulletsGroup.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            # increase level - as displayed on screen, pg. 295
            self.stats.level += 1
            self.sb.prep_level()
        
        
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
        #alien_width = alien.rect.width # alien.rect.width was used below for xpos anyway. i guess this just shortens it slightly
        #alien_fleet_spacing = alien.rect.height * 2
        # I rcreated the self.settings.fleet_ship_spacing as a variable in settings.py
        # so i could easily adjust it like everything else - note: 10px might be too much
        self.screen_rect = self.screen.get_rect() # make rectangle out of dimensions of window

        current_y = self.screen_rect.top# - alien.height
        current_x = self.screen_rect.right  - self.settings.fleet_ship_spacing
        
        alien.rect.y = current_y
        alien.y = current_y
        
        alien.rect.x = current_x
        alien.x = current_x

        alien_counter = 1
        while current_x >= float(self.settings.screen_width // 3) : #alien.x - (alien_width * 3):
            while current_y < ( self.settings.screen_height - (alien_height * 3)  ):
                print(f"value of alien_counter is {alien_counter}")

                my_alien = self._create_alien(current_y, current_x)
                print(f"my_alien[0] is {my_alien[0]} and my_alien[1] is {my_alien[1]}")

                current_y = my_alien[0] # 0 = my_alien bottom #+ self.settings.fleet_ship_spacing # inner while
                alien_counter += 1
                
            
            print(f"alien.y is {alien.y}")
            current_y = alien.y# - self.settings.fleet_ship_spacing  # outer while my_alien[0] - self.settings.fleet_ship_spacing # 
            current_x = my_alien[1] # - (alien_width * 1.5) # - self.settings.fleet_ship_spacing  

            print(f"out while after changing current_x/y, current_x is {current_x} and current_y is {current_y}")

            


    def _create_alien(self, current_y, current_x):
        """ Create an alien and place it in the row """
        #spawn an alien
        fleet_alien = Alien(self)

        # alien spacing from top of screen e.g. top = 0
        fleet_alien.rect.y = current_y + (fleet_alien.rect.height // 3) + self.settings.fleet_ship_spacing
        fleet_alien.y = float(fleet_alien.rect.y )

        
        # alien spacing from right side of screen e.g. subtract from total width of screen
        fleet_alien.rect.x  = current_x - fleet_alien.rect.width - self.settings.fleet_ship_spacing
        fleet_alien.x = float(fleet_alien.rect.x  )
        
        
        print(f"inside alien_create, fleet_alien.y of fleet_alien is {fleet_alien.y} and fleet_alien.rect.y is {fleet_alien.rect.y}")
        print(f"inside alien_create, fleet_alien.x of fleet_alien is {fleet_alien.x} and fleet_alien.rect.x is {fleet_alien.rect.x}")

        self.aliensGroup.add(fleet_alien)
        # could I just return the fleet alien itself? so I can access the bottom and left sides
        # from other loop? or just return fleet_alien.rect?
        #fleet_alien.rect
        print(f"fleet_alien.rect.bottom is {fleet_alien.rect.bottom} and fleet_alien.rect.left is {fleet_alien.rect.left}")
        return fleet_alien.rect.bottom, fleet_alien.rect.left
    

    def _check_aliens_left(self): # all the way right == loss (instead of bottom)
        """check if any aliens have reached the right of the screen"""
        # added pg 273/4 to check if fleet has reached bottom of screen
        for alien in self.aliensGroup.sprites(): #...group
# below customized from the ship at left version; to check if aliens have passed left edge of window
            if alien.rect.left <= 0: # all the way left == 0; to spell this out: alien reaches left of screen when alien's rect.left value >= screen's width
                self._ship_hit()
                break
    
    def _check_fleet_edges(self):
        """respond appropriately if any aliens have reached an edge"""
        for alien in self.aliensGroup.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """drop the entire fleet and change the fleet's direction (move left)"""
        for alien in self.aliensGroup.sprites(): # forgot to change to aliensGroup. again.
            #alien.rect.y += self.settings.fleet_drop_speed
            # just changed this to x
            # also, this should be moving to left/towards 0 so changed to -= insted of +=
            alien.rect.x -= self.settings.fleet_drop_speed # moving left would be negative as it'd be moving toward 0. right?
        
        # fleet movement working but going to right instead of left - changed this from -1 to 1...
        # okay this as postive 1 is very strange/unexpected result. I almost like it. don't do that.
        self.settings.fleet_direction *= -1 
    
    def _update_aliens(self):
        """update the positions of all aliens in the fleet"""
        self._check_fleet_edges()

        self.aliensGroup.update()
        
# spritecollideany - two arguments are a sprite and a sprite group: if the self.ship group collides with aliens group...hit
        if pygame.sprite.spritecollideany(self.ship, self.aliensGroup): # alienGROUP
                    #print("Ship hit!!!") # this was just here for testing
                    self._ship_hit()
        
        # look for aliens hitting the bottom of the screen
        self._check_aliens_left()
                
    def _ship_hit(self):
        """respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0: # part of game over edits, pg 274 (also with all the indenting)
            # method added per book pg 272
            # and update scoreboard (pg. 298)
            self.stats.ships_left -= 1
            self.sb.prep_ships() # save this for later/chap 14
            
            # Get rid of any remaining bullets and aliens -- GROUP
            self.bulletsGroup.empty()
            self.aliensGroup.empty()
            
            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            # pause
            sleep(0.5)
        
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
    

    def _update_screen(self):
        """update images on screen and flip to the new screen"""        
        self.screen.fill(self.settings.bg_color)
        
        for bullet in self.bulletsGroup.sprites():
            bullet.draw_bullet()
        
        self.ship.blitme()
        self.aliensGroup.draw(self.screen) # draw is alien group method
        # draw score info
        self.sb.show_score()
        
        #draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()
        
        
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