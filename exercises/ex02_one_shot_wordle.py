"""EX02 - One-Shot Wordle - Loops!"""

__author__ : "730466642"

secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")
length_secret: str = len(secret_word)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i : int = 0
emoji: str = ""

#check if guessed word is 6 letters long
while len(guess) != len(secret_word):
    guess = input(f"That was not {length_secret} letters! Try again: ")

while i < len(secret_word):
    #test to see if current index of guessed word is equal to the same index of secret word
    if guess[i] == secret_word[i]:
        emoji = emoji + GREEN_BOX
    else: 
        exists: bool = False
        alt_idx: int = 0
        while (exists is False) and (alt_idx < len(secret_word)):
            #test to see if letter exists in word
            if guess[i] != secret_word[alt_idx]:
                alt_idx = alt_idx + 1
            else:
                exists = True
        if exists is False:
            emoji = emoji + WHITE_BOX
        else:
            emoji = emoji + YELLOW_BOX
    i += 1
print(emoji)
if guess == secret_word:
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")




    
    

    

