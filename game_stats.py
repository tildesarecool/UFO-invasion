class GameStats:
    """Track statistics for Alien Invasion"""
    
    def __init__(self, ufoinv):
        """Initialize statistics"""
        self.settings = ufoinv.settings
        self.reset_stats()
        # high scores should never be reset
        self.high_score = 0
        self.level = 1
        
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        # this "left" refers to how many are left...not being on the left side...
        self.ships_left = self.settings.ship_limit
        self.score = 0 # added for scorring system, pg. 386
        