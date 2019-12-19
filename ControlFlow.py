"""
Programmer: Elle Green
Date: 12.16.19
Program: Guess My Number
"""

myNumber = 7

print("\nGuess a number between 1 & 10\n")

# Ask users to guess
guess = int(input('Enter a Guess: '))

# keep asking user to guess my number until they answer it correct
while guess != myNumber:
    guess = int(input("Enter a new number you got this: "))
print('Nice job you guessed it')
