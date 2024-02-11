#  24 jan 2023
#  alien invasion game from the book "python crash course"
# adopted into "ufo invasion" which is mostly alien invasion but roated 90 degrees so it's left/right
# i've hit the run to confirm that yes, it works prior to starting to work on things.
import sys, pygame
from time import sleep # added page 272
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien # modification for chapter 13 - bringing in the alien.py stuff

class AlienInvasion: 
    # Overall class to manage game assets and behavior 
    def __init__(self):
        # Initialize the game, and create game resources
        pygame.init()
        self.clock = pygame.time.Clock() # related to consistent frame rate - see also tick method
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (
            self.settings.screen_width, 
            self.settings.screen_height
            )
        )
        
        
        
        
        #self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("UFO Invasion")

        self.stats = GameStats(self)


        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() # create a group that holds the bullets 
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()

        self.game_active = True # this addition correlates to edits in _ship_hit() below

        # set background color
        #self.bg_color = (230,230,230)
        

# This is the code for full screen, which looks terrible on my giant monitor - page 245 - after implementing it the books says (paraphrasing)
# "but if that doesn't work good that keep the old code" - could have said that first!
#        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
#        self.settings.screen_width = self.screen.get_rect().width
#        self.settings.screen_height = self.screen.get_rect().height

        
        
    # per the book, methods that start with a _ are "helper methods"
    def run_game(self):    
        """start the main loop for the game"""
        while True:
            # when the update() is called on a group the group automatically calls update() for each sprite in the group
            self._check_events()
            if self.game_active: # added this if as part of "identifying when parts of the game should run" pg 275 - also indented method calls
                self.ship.update()
                self._update_bullets()
                self.bullets.update() # update position of bullets on each pass through while loop
            
            # get rid of bullets that have disappeared 
            #for bullet in self.bullets.copy(): # going through each bullet in the bulllet...list? bullets created each time space bar used, anyway
            #    if bullet.rect.bottom <= 0: # rect bottom:  the bullet is a rectangle, 0 is top of screen - this checks if bottom of bullet is out of visibility
            #        self.bullets.remove(bullet)
            # print(len(self.bullets)) # exists for debugging - should reduce to 0 once all the bullets have left the screen. verified as working so removed...

            self._update_aliens() # added for making fleet of aliens move, chapter 13
            self._update_screen()
            self.clock.tick(60) # related to consistent framerate - see also the self.clock line in the init function
            # Watch for keyboard and mouse events.
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
# ################################################################ #
    def _check_keydown_events(self, event):
        '''respond to keypresses'''
        if event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """repsond to key releases"""
        if event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False
            
    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed: # arbitrarily limit number of bullets on screen at once (page 251) see also bullets.py
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """update position of bullets and get rid of old bullets"""
        # update bullet position
        self.bullets.update()
        
        # get rid of bullets that have disappeared - swap this slightly so it's horizontal rather than vertical
        #for bullet in self.bullets.copy():
        #    if bullet.rect.bottom <= 0:
        #        self.bullets.remove(bullet)
        #self.bullets.copy
        for bullet in self.bullets.copy():
            #pass
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
                
        self._check_bullet_alien_collisions() # chapter stuff - bullet/alien collision, obviously

# ########################################################## #


    def _check_bullet_alien_collisions(self): # this method added as part of refactoring starting on page 269
        """respond to bullet-alien collisions"""
        #remove any bullets and aliens that have colided
        collisions = pygame.sprite.groupcollide( self.bullets, self.aliens, True, True ) # added as part of bullets/collision, pg. 267
        # per the book:
        # for a high powered bullet that can travel to the top of screen/destroy all enemies it encounters, set the first boolean to false
        # and keep the second boolean true.  would make that bullet active until it reached the top of the screen

        # part of spawning new fleet once fleet destroyed - pg. 268
        if not self.aliens:
            # destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        
        # look for alien ship collisions - pg 271
        if pygame.sprite.spritecollideany(self.ship, self.aliens): # spritecollideany - two arguments are a sprite and a sprite group: if the self.ship group collides with aliens group...hit
            # print("Ship hit!!!") # this was just here for testing
            self._ship_hit()
        
        # look for aliens hitting the bottom of the screen
        self._check_aliens_left() # checking leftward progress rather than bottomward progress

    def _ship_hit(self):
        """respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0: # part of game over edits, pg 274 (also with all the indenting)
            # decrement ships left - method added per book pg 272
# again, this NUMBER OF SHIPS LEFT as in a counter (not side of the screen)
            self.stats.ships_left -= 1
            
            # Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            
            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            # pause
            sleep(0.5)
        else:
            self.game_active = False




# ########################################################## #

    def _create_fleet(self):
        """create fleet of aliens"""
# ############# must redo this for different axis ################## #
        # make an alien
        alien = Alien(self)
        #alien_height = alien.rect.height
        alien_width, alien_height = alien.rect.size # get alien image width/height


# ########################################################## #
#self.rect.x = self.screen_rect.width - 100 # these two worked once i added the settings and screen_rect lines above
#self.rect.y = 10 #self.rect.height
# ########################################################## #

        #current_y = alien_height # this seems redundant since i set a value in alien.py (right?) that would explain the extra alien in addition to the fleet
# these two lines were sort of working from alien.py so I've commented them out there and put them
# here: current_y is 10 px down from top of screen and current_x is 100 pixels in from the right
# side of the screen
        current_y = 10
        current_x =  self.settings.screen_width - 100 # i think screen width minus 100 is what i was going for
        while current_y < (self.settings.screen_height + 2 * alien_height):
            #pass
            while current_x < (self.settings.screen_width - 2 * alien_width):
                #pass
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_height
            current_x = alien_width
            current_y += 2 * alien_height
    
    def _create_alien(self, x_position, y_position):
        '''create an alien and place it in the COLUMN'''
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
        
    def _check_aliens_left(self): # LEFT (where ship is) IN PLACE OF BOTTOM!!
        '''check if any aliens have reached the [left] of the screen'''
        for alien in self.aliens.sprites():
            if alien.rect.left <= self.settings.screen_width: # I'm hoping this will work for horizontal
                self._ship_hit()
                break
            
    def _check_fleet_edges(self):
        """respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed # minus is closer to left/ship, right? x is getting closer to 0??
# fleet_direction defined in settings.py 
# 1 == down, -1 == up
# so it starts as moving down then multiply that by neg 1 and you -1 or "up" e.g. "change direction"
        self.settings.fleet_direction *= -1 


        #while current_y < (self.settings.screen_height + 2 * alien_height):
        #    new_alien = Alien(self)
        #    new_alien.y = current_y
        #    new_alien.rect.y = current_y
        #    self.aliens.add(new_alien)
        #    current_y = current_y + 2 * alien_height
        #    self.aliens.add(alien)
        #    print(len(self.aliens))
        #pass

#    def _create_fleet(self):
  #      """create fleet of aliens"""
#        # make an alien
#        alien = Alien(self)
#        self.aliens.add(alien)
        #pass
    

    #def _create_alien(self, x_position, y_position):
    #    '''create an alien as place it in the row'''
    #    new_alien = Alien(self)
    #    new_alien.x = x_position
    #    new_alien.rect.x = x_position
    #    new_alien.rect.y = y_position
    #    self.aliens.add(new_alien) 



    def _update_screen(self):
        """update images on screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color) # 230,230,230 = light gray
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

            # Make the most recently drawn screen visible
        pygame.display.flip()

                
if __name__ == '__main__':
    
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
        