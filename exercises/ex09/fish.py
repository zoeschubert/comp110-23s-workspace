"""File to define Fish class."""
__author__ = "730466642"


class Fish:
    """Defines fish in the river."""
    
    age: int

    def __init__(self):
        """Initialize the age of the fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """Increase the age after a day."""
        self.age += 1
        return None