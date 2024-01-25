# alien.py
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
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # load the laien image and set its rect attribute - apparently using the / for the path to the image is really important
        self.image = pygame.image.load('images/alien.png') # load in the image
        self.rect = self.image.get_rect() # load in dimensions of the image
        
        # start each new alien near the top of the left of the screen
        # I guess 0,0 position
        # for horizontal i guess it'd be the top right corner
        # so vertical/y would 0 and horizontal/x would be (get screen width) - for top vertically and all the way on the right
        # self.rect.midleft = self.screen_rect.midleft # midleft didn't fill in so i don't know if this works
        #self.rect.upright = self.screen_rect.upright
        #self.rect.x = self.screen_rect.width - 100 # these two worked once i added the settings and screen_rect lines above
        #self.rect.y = 10 #self.rect.height
        ###########################################
        # okay how abou this: two variables for where i want the first alien to show up then plug them in
        
        #                                60 e.g. 60 px down from top. think this can just be 0
        #self.first_alien_y = self.rect.height # hopefully down the same amount as the image's height
        #self.first_alien_y = 0 # the number and spacing of the aliens is still wrong so not zero
        # self.first_alien_y = 30 # this is some how worse
        #                                       1200             60     - 10       == 1130
        #self.first_alien_y = (self.screen_rect.height - self.rect.height) - 10
        self.first_alien_y = self.screen_rect.top + 5
        self.first_alien_x = (self.screen_rect.width - self.rect.width) - 10
#        self.first_alien_x = self.screen_rect.width - (self.screen_rect.width - self.rect.width)
        
        #print(f"the screen width is {self.screen_rect.width}")
        
        print(f"self.rect.height is {self.rect.height}")
        print(f"self.first_alien_y is {self.first_alien_y }")
        print(f"the screen height is {self.screen_rect.height}")
        print(f"self.screen_rect.top is {self.screen_rect.top}")
        
        self.rect.x = self.first_alien_x
        self.rect.y = self.first_alien_y
        #self.rect.y = self.screen_rect.top + 5
        
        #self.rect.x = ai_game.sc
        
    def check_edges(self):
        """Return true if alien is at edge of screen. - method added chapter 13/pg 265"""    
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
        
    # this method was added for the "make the fleet move" section
    def update(self):
        """move the alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction # not sure if these settings.py variables are getting picked up or not
        #self.x += self.settings.alien_speed
        self.rect.x = self.x
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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