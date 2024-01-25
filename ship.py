# ship.py
# for the alien invasion script
# python crash course: ufo invasion
# implementing changes from chapter 13

# as i start modifying it, the main problem is the placement of the first alien ship. 
# i don't need a placement of single initial alien ship i just need the column of them, really
# did realize that the code was setting the screen coordinates of the alien image to the dimensions of the alien image
# which is perfect placement of the image in the corner but way too confusing
# some notes on rectangles from the pygame docs -
'''
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

class Ship:
    """a class to manage the ship"""
    def __init__(self, ai_game):
        """initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # load ship image and gets its rect.
        # the script kept failing by saying it can't find this image
        # then i closed/re-opened just the crashcrouse subdirectory in vscode and ran alient invasion.py and it worked
        # no idea why it didn't or started to run
        
        # the book seemed to make a big thing about using a BMP file versus using a jpg or png but from this experiement it seems both filetypes load without issue
        # so i'll just use the png
        #self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        
        # start each new ship at the bottom center of the screen.
        # pygame treats the image as rectangle
        # so rect.midbottom "bottom center of image file"
        # and this is set to the "bottom middle of the screen rectangle itself"
        # thus, the image is int he middle of the screen at the bottom
        # self.rect.midbottom = self.screen_rect.midbottom # original line
        
        
        # may want to adjust this so there's spacing between left side screen and back of ship.
        # get teh screen height, divide by 2 to get 'midleft' then add 10px so pixels from side or whatever(?)
        self.rect.midleft = self.screen_rect.midleft 
        
        
        # store a float for the ship's exact horizontal position
        # self.x = float(self.rect.x) # changing this y
        self.y = float(self.rect.y)
        #  Movement flag; start with a ship that's not moving
        # changing these two from left/right to top/bottom
        #self.moving_right = False
        #self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
        
    def update(self):
        """update the ship's position based on the movement flags."""
        # Update the ship's x value, not the rect
        # must change these also to up/down and from x to y        
        
        #if self.moving_right and self.rect.right < self.screen_rect.right: # right hand side is max x value - screen_rect.right
        #    self.x += self.settings.ship_speed
        # I think i got this backwords as i'm testing top vs 0
        #if self.moving_top and self.rect.top < self.screen_rect.top:
        #    self.y += self.settings.ship_speed
        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
            
        #if self.moving_left:
        #if self.moving_left and self.rect.left > 0: # left side is coord 0
        #    self.x -= self.settings.ship_speed
        # I think i got this backwords as i'm testing bottom vs window width, which is furthest from 0...rect bottom
        #if self.moving_bottom and self.rect.bottom > 0:
        #    self.y -= self.settings.ship_speed
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
            
        # update rect object from self.x
        #self.rect.x = self.x
        
        self.rect.y = self.y

        
    
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)