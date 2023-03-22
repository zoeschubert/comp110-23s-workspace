"""EX06 - Create your own adventure."""
__author__ = "730466642"


ISLAND: str = "\U0001F3DD"
MOUNTAIN: str = "\U0001F5FB"
TRAIL: str = "\U0001F6E4"
RIVER: str = "\U0001F6F6"
DIG: str = "\U0001FAA8"
CLIMB: str = "\U0001F9D7"
TREASUREONE: str = "\U0001F4B0"
TREASURETWO: str = "\U0001F48E"
location: str = ""
player: str = ""
points: int = 0


def main() -> None: 
    """The entrypoint to the program."""
    global player
    global points
    global location
    greet()
    print(f"Alright {player}, you can go to the island, the mountain, or neither. ")
    location = input("Choose 'mountain' or 'island' to go forth, or 'leave' if you wish to give up on this journey. ")
    while points < 30 and location != "done":
        if location == "island":
            island()
        else:
            if location == "mountain":
                points = mountain(points)
            else:  # this is where the player exits
                if location == "leave":
                    goodbye()
    if points >= 30 and location != "done":
            print(f"After {points} points accumulated, you found the treasure {TREASUREONE}{TREASURETWO}!")
    

def greet() -> None:
    """Welcome the player to the game."""
    global player
    player = input("What is your name? ")
    print(f"Welcome {player}! You will choose a location to begin your quest in finding the secret treasure.")


def island() -> None: 
    """The player comes to the island and makes next choice."""
    global player
    global points
    global location
    print(f"Aloha, {player}, you have reached the island {ISLAND}.")
    choice: str = input(f"Will you travel on the trail {TRAIL} or down the river {RIVER}? ")
    if choice == "trail":
        points += 15
    elif choice == "river":
        points += 10
    if points < 30: # the loop keeps going because player has not reached point threshold
        location = input(f"Okay traveler, you now have {points} points. Choose again from the 3 location choices. ")
    

def mountain(points: int) -> int:
    """The player comes to the mountain and makes next choice."""
    global player
    global location
    from random import randint
    print(f"Hello, {player}, you have reached the mountain {MOUNTAIN}.")
    choice: str = input(f"Will you dig {DIG} or climb {CLIMB}? ") 
    if choice == "dig": 
        points += 15
    elif choice == "climb":
            points -= randint(0, 10)
    if points < 30: # the loop keeps going because player has not reached point threshold
        location = input(f"Okay traveler, you now have {points} points. Choose again from the 3 location choices. ")
    return points


def goodbye() -> None: 
    """Bid the player farewell since they chose to leave."""
    global player
    global points
    global location
    print(f"Sorry, {player}, you got {points} points and did not find the treasure. Goodbye!")
    location = "done"


if __name__ == "__main__":
    main()