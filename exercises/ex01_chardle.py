"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730466642"

guessed_word: str = input("Enter a 5-character word: ")
if(len(guessed_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
letter_in_word: str = input("Enter a single character: ")
if(len(letter_in_word) != 1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for "+ letter_in_word +" in "+ guessed_word)

i: int = 0
counter: int = 0

if(letter_in_word == guessed_word[i]):
    print(f"{letter_in_word} found at index 0")
    counter += 1
i += 1
if(letter_in_word ==guessed_word[i]):
    print(f"{letter_in_word} found at index 1")
    counter += 1
i += 1
if(letter_in_word == guessed_word[i]):
    print(f"{letter_in_word} found at index 2")
    counter += 1
i += 1
if(letter_in_word == guessed_word[i]):
    print(f"{letter_in_word} found at index 3")
    counter += 1
i += 1
if(letter_in_word == guessed_word[i]):
    print(f"{letter_in_word} found at index 4")
    counter += 1
if(counter == 0):
    print(f"No instances of {letter_in_word} found in {guessed_word}")
if(counter == 1):
    print(f"{counter} instance of {letter_in_word} found in {guessed_word}")
else:
    print(f"{counter} instances of {letter_in_word} found in {guessed_word}")
