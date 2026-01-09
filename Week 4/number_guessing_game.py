"""
Write a Python program for a number guessing game where the
computer chooses a random number between 1 and 20, and the player
has five chances to guess the number. Use a for loop to limit the
number of guesses the player can make. After each guess, the program
should tell the player whether the guess was too high or too low. If the
player correctly guesses the number, the program should congratulate
the player and end the game. If the player runs out of guesses, the
program should reveal the number and show the player's guesses
"""

import random

rand_num = random.randint(1,20)

for i in range(5, 0, -1):
    print(f"You have {i} chances left")
    guess = int(input("Enter your guess(1-20): "))
    if guess < rand_num:
        print("You guess too low")
    elif guess > rand_num:
        print("You guess too high.")
    else:
        print(f"Your guess {guess} is correct!")
        break
