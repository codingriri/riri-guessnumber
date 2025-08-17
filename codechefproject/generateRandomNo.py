import random

def getRandomNumber():
    n = random.randrange(1,100)
    return n


def runGuess():
    secretNumber = getRandomNumber()
    print("The number is", secretNumber)


if __name__ == '__main__':
    runGuess()
