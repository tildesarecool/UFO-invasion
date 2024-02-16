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

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    
    def __init__(self, ufoinv_game):
        """create a bullet object at teh ship's current position"""
        super().__init__()
        self.screen = ufoinv_game.screen
        self.settings = ufoinv_game.settings
        self.color = self.settings.bullet_color
        
        # create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                               self.settings.bullet_height)
        #self.rect = pygame.Rect()
        #self.bullet_width = 15 # was 3 # (i pasted this from settings so i had a reference)
        #self.bullet_height = 3 # was 15 # (i pasted this from settings so i had a reference)
        #self.rect.midtop = ufoinv_game.ship.rect.midtop # middle/top of the ship sprite
        
        # must change this for horizontal
        # self.rect.midtop = ufoinv_game.ship.rect.midright # middle/right of the ship sprite
        
        # with the big height debug size bullets, lining a bullet midleft with the ship's mid right made sense (and it works)
        # i think this is the only chap 13 edit needed for bullet.py
        #self.rect.midleft = ufoinv_game.ship.rect.midright 
        self.rect.midright = ufoinv_game.ship.rect.midright 
        
        # this has to be change to be x
        #store the bullet's psition as a float
        # self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    
    def update(self):
        """move the bullet up the screen"""
        # update the exact position of the bullet
        # also must be x
        # self.y -= self.settings.bullet_speed
        self.x += self.settings.bullet_speed
        # update the rect position
        #self.rect.y = self.y
        self.rect.x = self.x
        
    def draw_bullet(self):
        """draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)