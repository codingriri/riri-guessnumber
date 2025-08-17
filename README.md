# Hot & Cold Number Guesser

A simple command-line game where you guess a number between 1 and 100, and the system gives you "Hot" or "Cold" feedback.

## 🎯 Features

* **Random Number Generation:** The computer chooses a random number from 1 to 100.
* **Hot & Cold Feedback:**
    * 'Hot' if your guess is within a 10-unit range of the number.
    * 'Cold' if your guess is more than 10 units away.
* **High/Low Hints:** The game tells you if your guess is too high or too low.
* **Guess Counter:** Tracks and displays how many guesses you took to find the correct number.

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/number-guesser.git](https://github.com/yourusername/number-guesser.git)
    cd number-guesser
    ```
2.  **Run the game:**
    ```bash
    python game.py
    ```

## 🎮 How to Play

1.  The computer will pick a secret number.
2.  Enter your first guess when prompted.
3.  Based on your guess, you will receive feedback:
    * "Hot!"
    * "Cold"
    * "Correct! You guessed the number in n attempts."
4.  Keep guessing until you find the number. The game will tell you how many attempts it took.

## ⌨️ Sample Input/Output

Here's an example of a game session. (Assume the secret number is 42)

**Output:**
Welcome to the Hot & Cold Number Guesser!
I have picked a secret number between 1 and 100.
Guess a number:

**Input:**
50

**Output:**
Hot!
Guess a number:

**Input:**
30

**Output:**
Hot!
Guess a number:

**Input:**
42

**Output:**
Correct! You guessed the number in 3 attempts.

## 📜 License

This project is licensed under the MIT License.
