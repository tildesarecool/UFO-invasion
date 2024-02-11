import pygame, sys
from ship import Ship

# forgot minor detail of changing all the left/right to update/down



class GameEvents:
    def __init__(self, ufoinv_game): 
        """doing events from another class"""
        #self.ship = Ship(self)
        
        self.screen = ufoinv_game.screen
        self.screen_rect = ufoinv_game.screen.get_rect()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
#            elif event.type == pygame.KEYDOWN:
#                self._check_keydown_events(event)
#            elif event.type == pygame.KEYUP:
#                self._check_keyup_events(event)
            # haven't made it to buttons and mouse events yet
            # so I'll leave this for later
            #elif event.type == pygame.MOUSEBUTTONDOWN:
            #    mouse_pos = pygame.mouse.get_pos()
            #    self._check_play_button(mouse_pos)


    # i am realizing i'm going to need to import the ship class
    # in order for this to work. no big deal(?)
    # ok well self.ship isn't going to work now is it
    # i haven't defined the various moving methods anyway
    # with the above ship = Ship() line and
    # ship.moving_right = True
    # the ship was syntax highlighted so maybe that'd work...?
    
    # I added in the __init__ method above using a similar format to ship.py
    # then left everything in other methods as self.ship etc
    
 #   def _check_keydown_events(self, event):
 #       '''respond to keypresses'''
 #       if event.key == pygame.K_RIGHT:
 #           self.ship.moving_right = True
 #       elif event.key == pygame.K_LEFT:
 #           self.ship.moving_left = True
 #       elif event.key == pygame.K_q:
 #           sys.exit()
 #       elif event.key == pygame.K_SPACE:
 #           self._fire_bullet()
    
 #   def _check_keyup_events(self, event):
 #       """repsond to key releases"""
 #       if event.key == pygame.K_RIGHT:
 #           self.ship.moving_right = False
 #       elif event.key == pygame.K_LEFT:
 #           self.ship.moving_left = False