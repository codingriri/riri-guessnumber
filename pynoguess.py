import random

# Generates a random number between 1 and 99 (inclusive)
def getRandomNumber():
    return random.randrange(1, 100)

# Compares the user's guess to the secret number and provides a hint:
# - "Right" if the guess is correct
# - "Cold" if the guess is more than 10 away
# - "Hot" if the guess is within ±10 range
def giveHint(number, guess):
    if guess > (number + 10) or guess < (number - 10):
        return "Cold"
    elif number == guess:
        return "Right"
    else:
        return "Hot"

# Main function to run the guessing game
def runGuess():
    secretNumber = getRandomNumber()
    user_guess = int(input("Enter a number between 1 and 100: "))
    # To count the number of guessing attempts
    guessCounter=0
    while True:
        hint = giveHint(secretNumber, user_guess)
        guessCounter+=1
        if hint == "Right":
            print("You guessed it Right!")
            break
        else:
            print(hint)
            user_guess = int(input("Enter number again: "))
            
            
if __name__ == '__main__':
    runGuess()
