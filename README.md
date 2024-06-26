# Learning Python Progressively

## Introduction

We are going to practice the basic of Python programming using a simple text-based game, called "Guess the Number" game. This program helps reinforce concepts like:

- Variables
- Functions
- Loops
- Conditionals
- User input
- Library Imports

## Guess the Number Game

To run the program use **_ python guess_the_number.py _**

### Import necessary modules:

      random module to generate a random number.

### Generate a random number:

        Use random.randint() to generate a random number between 1 and 100.

### Set up the game loop:

        Use a while loop to keep the game running until the player guesses the number.

### Get user input:

        Use input() to get the player's guess.

### Compare the guess to the random number:

        Use if-elif-else statements to compare the guess and provide feedback (e.g., "Too high," "Too low," or "Correct").

### End the game:

        Break out of the loop when the player guesses correctly.

## Key Concepts Practiced

- _Importing Modules:_ Using the import statement to include the random module.
- _Random Number Generation:_ Using random.randint() to generate a number.
- _Loops:_ Using a while loop to keep the game running until the condition is met.
- _Conditionals:_ Using if-elif-else statements to compare the user's guess and provide feedback.
- _User Input:_ Using input() to get data from the user and isdigit() to validate it.
- _Type Conversion:_ Converting the input string to an integer with int().

# Assignment

1. Create a new branch named "assignment1"
2. Create a new file named "assignmentone.py"

3. Let's make it a "Word Guessing Game." In this game, the player has to guess a word chosen randomly from a predefined list of words. The player is given a certain number of attempts to guess the word correctly.

### Word Guessing Game

- _Define a list of words:_ Create a list of words from which the program will randomly select one.
- _Randomly select a word:_ Use the random module to select a word from the list.
- _Set up the game loop:_ Use a loop to allow the player to guess the word within a certain number of attempts.
- _Get user input:_ Use the input() function to get the player's guess.
- _Provide feedback:_ Inform the player if their guess is correct or not, and how many attempts remain.
- _End the game:_ Either when the player guesses the word correctly or runs out of attempts.

4. Finally commit and push your work to the newly created branch "assigment1" this will create a branch to the remote repository.
