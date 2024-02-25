# settings.py - settings for alien invasion script

import json # these two lines added as part of new save-to-json
import os   # functinality added 15 feb 2024 (not in book)

class Settings:
    """a class to store all settings for alien invasion"""
    def __init__(self):
        """initialize game's [static] settings."""
        
        #self.initialize_dynamic_settings()
        self.load_settings_from_json("settings.json") # changig settings here doesn't auto-change json. might have to adjust that -feb24

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        # ship settings
        #self.ship_speed = 4.5 # this actually only accepts ints so adjustments were made to ship.py
        self.ship_limit = 3
        # bullet settings
        #self.bullet_speed = 6.0
        self.bullet_width = 15 # default value = 15 - a good value for test is 300
        self.bullet_height = 450 # default =3; height would be higher for debug, right? 
        self.bullet_color = (60, 60, 60) # 60, 60, 60 is "dark gray" (apparently 000 = black and 255 255 255 = white)
        self.bullets_allowed = 9 # default value = 3 arbitrarily limit number of bulets on screen at once (page 251)
        # alien settings
        self.alien_speed = 1.0 # uncommented to make following chapter 13 easier, temporory/not really needed
        self.fleet_drop_speed = 10 # default value = 10 - setting this to 100 for debug purposes
        
        # this i came up with all on my own - see settings.py and 
        # the _create_fleet() method in ufo-invasion.py
        self.fleet_ship_spacing = 15
        
        # how quickly the game speeds up 
        self.speedup_scale = 1.1
        
        # How quickly the alien point values increase 
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
                
        
    def initialize_dynamic_settings(self):
        """initialize settinsg that change throughout the game"""
        self.ship_speed = 1.5 # 4.5 seems like a good setting
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        
        # this is all relative to y position. 
        # since "top" of window = 0, +1 is away from top e.g. "down 
        # and -1 is towards top. or "up"
        
        # as 1 from top/bottom version of this the fleet is moving right instead of left
        
        self.fleet_direction = 1
        
        # scoring settings
        self.alien_points = 50
        
    def increase_speed(self):
        """increase speed and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)

#### this is some settings/json code i got from chatgpt 15 feb 2024 (not in book)
#### a lot less code than I thought, actually - well i had to re-write parts of it. 

    def load_settings_from_json(self, filename):
        """Load settings from settings.json if it exists."""
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as file:
                    settings_dict = json.load(file)
                    
                for key, value in settings_dict.items():
                    setattr(self, key, value)
                self.initialize_dynamic_settings()
            except Exception as e:
                print(f"Error loading settings from JSON file: {e}")
        else:
            print(f"Settings JSON file not found. Using default settings.")
            self.initialize_dynamic_settings()


    def save_settings_to_json(self, filename):
        """Save settings to settings.json."""
        settings_dict = self.__dict__
        with open(filename, 'w') as file:
            json.dump(settings_dict, file, indent=4)



    '''
    def save_settings_to_json(self, filename):
        #"""Save settings to a JSON file."""
        settings_dict = {
            "screen_width": self.screen_width,
            "screen_height": self.screen_height,
            "bg_color": self.bg_color,
            "ship_limit": self.ship_limit,
            "bullet_width": self.bullet_width,
            "bullet_height": self.bullet_height,
            "bullet_color": self.bullet_color,
            "bullets_allowed": self.bullets_allowed,
            "fleet_drop_speed": self.fleet_drop_speed,
            "fleet_ship_spacing": self.fleet_ship_spacing,
            "speedup_scale": self.speedup_scale,
            "score_scale": self.score_scale,
            "ship_speed": self.ship_speed,
            "bullet_speed": self.bullet_speed,
            "alien_speed": self.alien_speed,
            "fleet_direction": self.fleet_direction,
            "alien_points": self.alien_points
        }
        with open(filename, 'w') as file:
            json.dump(settings_dict, file)
            
    def load_settings_from_json(self, filename):
        #"""Load settings from a JSON file."""
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as file:
                    settings_dict = json.load(file)
                # Update settings with values from the JSON file
                self.screen_width = settings_dict.get("screen_width", self.screen_width)
                self.screen_height = settings_dict.get("screen_height", self.screen_height)
                self.bg_color = tuple(settings_dict.get("bg_color", self.bg_color))
                self.ship_limit = settings_dict.get("ship_limit", self.ship_limit)
                self.bullet_width = settings_dict.get("bullet_width", self.bullet_width)
                self.bullet_height = settings_dict.get("bullet_height", self.bullet_height)
                self.bullet_color = settings_dict.get("bullet_color", self.bullet_color)
                self.bullets_allowed = settings_dict.get("bullets_allowed", self.bullets_allowed)
                self.fleet_drop_speed = settings_dict.get("fleet_drop_speed", self.fleet_drop_speed)
                self.fleet_ship_spacing = settings_dict.get("fleet_ship_spacing", self.fleet_ship_spacing)
                self.speedup_scale = settings_dict.get("speedup_scale", self.speedup_scale)
                self.score_scale = settings_dict.get("score_scale", self.score_scale)
                self.ship_speed = settings_dict.get("ship_speed", self.ship_speed)
                self.bullet_speed  = settings_dict.get("bullet_speed", self.bullet_speed)
                self.alien_speed = settings_dict.get("alien_speed", self.alien_speed)
                self.fleet_direction = settings_dict.get("fleet_direction", self.fleet_direction)
                self.alien_points = settings_dict.get("alien_points", self.alien_points)
                

                
                # Update other settings similarly
            except Exception as e:
                print(f"Error loading settings from JSON file: {e}")
        else:
            print("Settings JSON file not found. Using default settings.")
    '''