import random
# Number guessed by Computer
def getRandomNumber():
    return random.randrange(1, 100)

# Comparing the user's guessed number and the number by Computer
def giveHint(number, guess):
    if number == guess:
        return "Right"
    
    # Calculate the absolute difference to handle guesses above or below the number
    diff = abs(number - guess)
    
    # Check for the 'Hot' condition (within 10, inclusive)
    if diff <= 10:
        return "Hot"
    
    # All other cases are 'Cold'
    else:
        return "Cold"


def runGuess():
    secretNumber = getRandomNumber()
    user_guess = int(input("Enter a number between 1 and 100: "))
    hint = giveHint(secretNumber, user_guess)
    if hint == "Right":
        print("You guessed it Right!")
    else:
        print(hint)
            
if __name__ == '__main__':
    runGuess()
