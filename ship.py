# ship.py
# for the alien invasion script
# python crash course
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
from pygame.sprite import Sprite # save this for later


class Ship(Sprite): # decided to start over for the ship class
    """a class to manage the ship"""
    # I used ufoinv_game as substitute for ai_game in original. When creating instance of ship object "self is passed in" 
    # in original version from book
    def __init__(self, ufoinv_game): 
        """initialize the ship and set its starting position"""
        super().__init__()
        # some how i missed that these were set in the init method
        # so it didn't work. they just belong in the init method
        self.moving_up = False
        self.moving_down = False
        # this is rotated 90 degree version. instead of 'midbottom' it's 'midleft'
        
        # these four seems like boiler plate at this point
        
        # ufoinv_game is only defined when this ship object is instantiated 
        # which i think is why the syntax highlighting isn't kicking in: it doesn't know if it as a .screen or 
        # a .screen.get_rect
        # while the self.image and self.rect do get syntax highlighting
        # since they're coming off of pygame, an already imported library above
        # and the same for self.screen_rect.midleft below
        self.screen = ufoinv_game.screen
        self.settings = ufoinv_game.settings 
        self.screen_rect = ufoinv_game.screen.get_rect()
        
        # load ship image and assign a rect to the rect of the image
        # I assume that's what the line self.rect = self.image.get_rect()
        # actually does: create a new rectangle the width/height of the image?
        # "self" is referring the "the ship only" rect is for rectangle then the =
        # then the previously established self.image which is assigned the load method for the png in the filesystem
        # so logically...self.rect is a rectangle the shap of the ship image. final answer.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # since self.rect has been assigned the value of the get_rect() method
        # this self.rect.midleft should give me access to this predefined "attribute" of midleft
        
        # this is saying "assign the midleft of the ship's rectangle to the midleft of the screen's rectangle"
        self.rect.midleft = self.screen_rect.midleft
        
        # store float for ship's exact horizontal position 
        self.y = float(self.rect.y)
        
        
    def blitme(self):
        """draw the ship at its current location"""
        
        
        self.screen.blit(self.image, self.rect)
        
        
    
    # this will come in much later, just prepping it so it's here. also have to re-adjust for vertical orientation
    def center_ship(self): # added book page 273 as part of resetting when alien collides with ship
        """center ship on the screen (vertical/y)"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        #self.x = float(self.rect.x)
    
    
    
    def update(self):
        """update the ship's [VERTICAL] position based on the movement flags."""
        # updat the ship's y value, not the rect
                            # refers to side of rectangle - top
        #if self.moving_up and self.rect.top < self.screen_rect.top:
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
            #self.rect.y -= 1 # re-adjusted to decrease value so it move towards 0/top of screen
            
                            # refers to side of rectangle - bottom
        #if self.moving_down and self.rect.bottom > 0:
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            #self.rect.y += 1
            self.y += self.settings.ship_speed
        
        # update rect object from self.y
        self.rect.y = self.y
            