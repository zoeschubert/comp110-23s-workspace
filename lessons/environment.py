"""Example environment diagram program."""

secret: int = 3
guess: int = 2

if guess == secret:
    print("Succes!")
    print(str(guess) + " is the secret number!")
else:
    guess = guess + 1
    if guess == secret: 
        print("Success on 2nd try!")
    else:
        print("Wrong guess. :(")
        if (guess == secret - 1):
            print("Hint: The guess of " + str(guess) + " is off by only one number!")
