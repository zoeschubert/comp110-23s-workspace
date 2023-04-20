"""File to define River class."""

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear

__author__ = "730466642"


class River:
    """Class for the river with bears and fish."""
    
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove aging animals from the river."""
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []
        for elem in self.fish:
            if elem.age <= 3: 
                surviving_fish.append(elem)
            self.fish = surviving_fish
        for item in self.bears:
            if item.age <= 5:
                surviving_bears.append(item)
            self.bears = surviving_bears
        return None
    
    def remove_fish(self, amount: int):
        """Remove the frontmost fish."""
        for i in range(0, min(len(self.fish), amount)):
            self.fish.pop(0)

    def bears_eating(self):
        """Remove fish when bears eat."""
        for elem in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                elem.eat(3)
        return None
    
    def check_hunger(self):
        """Check the hunger scores to see which bears survive."""
        surviving_bears: list[Bear] = []
        for elem in self.bears: 
            if elem.hunger_score >= 0:
                surviving_bears.append(elem)
        self.bears = surviving_bears
        return None
        
    def repopulate_fish(self):
        """Add fish to the river as they reproduce."""
        fish_offspring: int = (len(self.fish) // 2) * 4
        i: int = 0
        while i < fish_offspring:
            self.fish.append(Fish())
            i += 1
        return None
    
    def repopulate_bears(self):
        """Add bears to the river as they reproduce."""
        offspring: int = len(self.bears) // 2
        i: int = 0
        while i < offspring:
            self.bears.append(Bear()) 
            i += 1
        return None
    
    def view_river(self):
        """Introduction to the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Call one river day seven times."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.day = 7
