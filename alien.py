import pygame
from pygame.sprite import Sprite
# this file added in chapter 13, if that wasn't obvious

# this already various from the book anyway
# but i'm modifying htis heavily so the alien starts at the upper right instead of the upper left
# I assume the right part would be the width of the window

class Alien(Sprite):
    """a class to represent a singal alient in the fleet"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        # i couldn't set the first alien coordsuntil i added these two below lines
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # load the laien image and set its rect attribute - apparently using the / for the path to the image is really important
        self.image = pygame.image.load('images/alien.png') # still have to make rotated 90 degrees version
        
        self.rect = self.image.get_rect()
        
        # start each new alien near the top of the left of the screen
        # I guess 0,0 position
        # for horizontal i guess it'd be the top right corner
        # so vertical/y would 0 and horizontal/x would be (get screen width) - for top vertically and all the way on the right
        # self.rect.midleft = self.screen_rect.midleft # midleft didn't fill in so i don't know if this works
        #self.rect.upright = self.screen_rect.upright
        
        # ########################################################## #
        #self.rect.x = self.screen_rect.width - 100 # these two worked once i added the settings and screen_rect lines above
        #self.rect.y = 10 #self.rect.height
        # ########################################################## #

        #self.rect.y = self.screen_rect.top
        
        # store the alien's exact horizontal position
        #self.x = float(self.rect.x)
        
        # #################################################################### #
        # what would the y coord look like? is that necessary?
        #self.screen_rect.top
        #self.y = float(self.rect.y)
        
        # ya, seems right
        
'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # start each new ship at the bottom center of the screen.
        # pygame treats the image as rectangle
        # so rect.midbottom "bottom center of image file"
        # and this is set to the "bottom middle of the screen rectangle itself"
        # thus, the image is int he middle of the screen at the bottom
        # self.rect.midbottom = self.screen_rect.midbottom # original line
        self.rect.midleft = self.screen_rect.midleft # midleft didn't fill in so i don't know if this works
        
        # store a float for the ship's exact horizontal position
        # self.x = float(self.rect.x) # changing this y
        self.y = float(self.rect.y)
        #  Movement flag; start with a ship that's not moving
        # changing these two from left/right to top/bottom
        #self.moving_right = False
        #self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
'''