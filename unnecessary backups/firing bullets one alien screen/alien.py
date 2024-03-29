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
        # I can't believe i figured out these two lines all by myself(tm)
        self.screen_rect = self.screen.get_rect()
        # the extra 20 px is to make sure no part of the alien is too far to right to see on screen
        self.xpos = self.screen_rect.width - self.rect.width - 20
        
        self.rect.x = self.xpos # self.screen_rect.right
        self.rect.y = self.rect.height
        # store the alien's exact horizontal position
        # I think what this is doing is using the width of the image rectangle
        # as the x coordinate for the screen position
        # so if the image was 100x100px the x screen coord would be 100px from the left
        # that's both clever and some how unintuitive at the same time
        self.y = float(self.rect.y) # changed this from .x to .y
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
########### this is the original/left right version. I'm going to make a new version and leave it commented out until it's needed
#    def update(self):
#        """move the alien to the right"""
#        self.x += self.settings.alien_speed * self.settings.fleet_direction # not sure if these settings.py variables are getting picked up or not
#        self.rect.x = self.x
        

############ re-done version for vertical playing
    # ok all i changed was self.x to self.y...but maybe that's all that's needed
    def update(self):
        """ move alien(s) up/down screen """
        self.y += self.settings.alien_speed * self.settings.fleet_direction
#        pass
