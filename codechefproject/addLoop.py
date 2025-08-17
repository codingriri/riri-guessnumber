import random

def getRandomNumber():
    return random.randrange(1, 100)

def giveHint(number, guess):
    if guess > (number + 10) or guess < (number - 10):
        return "Cold"
    elif number == guess:
        return "Right"
    else:
        return "Hot"

def runGuess():
    secretNumber = getRandomNumber()
    user_guess = int(input("Enter a number between 1 and 100: "))
    # Added loop to keep the game running unless user correctly guesses
    while True:
        hint = giveHint(secretNumber, user_guess)
        if hint == "Right":
            print("You guessed it Right!")
            break
        else:
            print(hint)
            user_guess = int(input("Enter number again: "))
            
            
if __name__ == '__main__':
    runGuess()
