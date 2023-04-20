"""File to define Bear class."""
__author__ = "730466642"


class Bear:
    """Class defining bears in the river."""
    
    age: int
    hunger_score: int

    def __init__(self):
        """Initialize the bear's hunger score."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Increase the age and hunger score after one day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Increase hunger score when bear is eating."""
        self.hunger_score += num_fish
        return None