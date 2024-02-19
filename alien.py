'''
This should probably universal reference at this point

The Rect object has several virtual attributes which can be used to move and align the Rect:
x,y
top, left, bottom, right
topleft, bottomleft, topright, bottomright
midtop, midleft, midbottom, midright
center, centerx, centery
size, width, height
w,h


All of these attributes can be assigned to: 
rect1.right = 10
rect2.center = (20,30)
'''




import pygame
from pygame.sprite import Sprite
# this file added in chapter 13, if that wasn't obvious
class Alien(Sprite):
    """a class to represent a singal alient in the fleet"""
    def __init__(self, ufoinv):
        super().__init__()
        self.screen = ufoinv.screen
        self.settings = ufoinv.settings
        # load the laien image and set its rect attribute - apparently using the / for the path to the image is really important
        self.image = pygame.image.load('images/alien.png') # still have to make rotated 90 degrees version
        self.rect = self.image.get_rect()
        # self is "the alien", rect is the rectangle based on the dimensions of the alien
        # so self.x is the position of the alien on the left versus right side of the screen
        # these two lines set the coords of the alien to the upper left effectively
        # but i want the x to be the right so x atleast has to be change
        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height
        #
        
        # I'm trying some new things. so this line a a few below are moving over to 
        # the create alien/create fleet methods in ufo-invasion.py
        #self.screen_rect = self.screen.get_rect()
        
        # in alien class 'self' is 'alien' outside of said alien class...
        # except for the screen stuff. i assume that's the window dimensions related
        # so self.xpos is alien.xpos and self.screen_rect.width is the width gathered from the settings file
        # via above line 
        # self.screen = ufoinv.screen
        # (right?)
        #self.xpos = self.screen_rect.width - self.rect.width - 20
        #self.rect.x = float(self.xpos) # self.screen_rect.right        
        
        
        # since the ship and the ship rectangle are the same and the fleet position is relative to that that is adjusted here
        # maybe i should just make this a setting? # self.fleet_ship_spacing note: see settings.py, made it a note
        # the self.settings.fleet_ship_spacing wasn't working from here so i moved the - self.settings.fleet_ship_spacing 
        # over to the _create_fleet() method in ufo-invasion
        
        
        #self.rect.y = self.rect.height #- self.settings.self.fleet_ship_spacing
        # store the alien's exact horizontal position
        # I think what this is doing is using the width of the image rectangle
        # as the x coordinate for the screen position
        # so if the image was 100x100px the x screen coord would be 100px from the left
        # that's both clever and some how unintuitive at the same time
        #self.y = float(self.rect.y) # moved this over to create fleet in main script
        # #################################################################### #
        # what would the y coord look like?
        # self.y = float(self.rect.y)
        # ya, seems right
    def check_edges(self):
        """Return true if alien is at edge of screen. - method added chapter 13/pg 265"""    
        screen_rect = self.screen.get_rect() # this is how you grab the screen so all the predefined bottom/top/right/bottomright predefines work
        #return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
        # this should be related to where the alien can go in the y dimension, so I'm adusting it
        return (self.rect.top <= 0) or (self.rect.bottom >= screen_rect.bottom)
        
    # this method was added for the "make the fleet move" section

############ re-done version for vertical playing
    # ok all i changed was self.x to self.y...but maybe that's all that's needed
    def update(self):
        """ move alien(s) up/down screen """
        self.y += self.settings.alien_speed * self.settings.fleet_direction
#        pass
