"""
Programmer: Elle Green
Date: 12.16.19
Program: Guess My Number


myNumber = 7

print("\nGuess a number between 1 & 10\n")

# Ask users to guess
guess = int(input('Enter a Guess: '))

# keep asking user to guess my number until they answer it correct
while guess != myNumber:
    guess = int(input("Enter a new number you got this: "))
print('Nice job you guessed it')
"""
# --------------------------------------------------------------------------------------------

"""
Programmer: Elle Green
Date: 12.19.19
Program: 1 through 10
"""

x = 1

# While Loop will see if a condition has been met
# If not it will run again until the condition is met

while x <= 10:
    print(x)
    x = x + 1
