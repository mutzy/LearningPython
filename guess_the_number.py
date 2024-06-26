# Importing libraries used to help in borrowing some functionality without wring code.
import random


# This is an example function in python
# Functions have the syntax "def {function_name}():"
# Always remember to used tab when writing your code otherwise set your IDE to the same for simplicity ask if you need help.

def guess_the_number():

    # Generate a random number between 1 and 100
    # This are example variables in python

    number_to_guess = random.randint(1, 100)
    attempts = 0

    # This is how you display a message on screen for the user
    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")

    # Start the game loop
    # This is an example of use of loops
    while True:
        # Get the player's guess
        # Here you are using the input function to display a message to the user and wait for user input
        # The user input value is then stored in the guess variable

        guess = input("Enter your guess: ")

        # Check if the input is a valid number
        # This is a use case for conditionals if something do something else continue
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        # Compare the guess to the number
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            # Having values in {} this are dynamic variables and change unlike the text beside it also notice the "f" before congratulations.
            print(
                f"Congratulations! You guessed the number in {attempts} attempts.")
            break


# Run the game
# This calls the above function and excutes it when this program is run.
guess_the_number()
