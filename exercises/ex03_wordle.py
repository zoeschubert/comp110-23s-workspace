"""EX03 - Structured Wordle"""
__author__ = "730466642"

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    exp_length: int = 5
    turns: int = 1
    guess: str = ""
    while secret != guess and turns <= 6:
        #go through turns when guesses are incorrect
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(exp_length)
        print(emojified(guess, secret))
        turns += 1
    if secret == guess:
        print(f"You won in {turns-1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
    


def contains_char(secret: str, guessed_char: str)->bool:
    """Check to see if the letter exists in the word"""
    assert len(guessed_char) == 1
    i: int = 0
    while i < len(secret):
        #check each index of the word until a guessed character matches
        if secret[i] == guessed_char:
            return True
        else: 
            i+=1
    return False
    

def emojified(guess: str, secret: str)->str:
    """Print emojis corresponding with guessed letters"""
    assert len(guess) == len(secret)
    i: int= 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    while i < len(secret):
        #test if current index of guessed word is equal to the same index of the secret word
        if guess[i] == secret [i]:
            emoji = emoji + GREEN_BOX
        else:
            if contains_char(secret, guess[i]) == True:
                emoji = emoji + YELLOW_BOX
            else: #no character found in secret
                emoji = emoji + WHITE_BOX
        i+=1
    return emoji

def input_guess(exp_length: int)->str: 
    """Check the length of the input guess"""
    guess = input(f"Enter a {exp_length} character word: ")
    while len(guess) != exp_length: 
        #check if word is expected length
        guess: str = input(f"That wasn't {exp_length} chars! Try again: ") 
    return guess


if __name__ == "__main__":
    main()


    