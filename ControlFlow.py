# Programmer: Elle Green
# Date: 12.16.19
# Program: Guess My Number

myNumber = 7

print("\nGuess a number between 1 & 10\n")

# Ask users to guess
guess = int(input('Enter a Guess: '))

# keep asking user to guess my number until they answer it correct
while guess != myNumber:
    guess = int(input("Enter a new number you got this: "))
print('Nice job you guessed it\n')

# --------------------------------------------------------------------------------------------
# Programmer: Elle Green
# Date: 12.19.19
# Program: 1 through 10

x = 1

# While Loop will see if a condition has been met
# If not it will run again until the condition is met

while x <= 10:
    print(x)
    x+=1


# Programmer: Elle green
# Date: 1-6-20
# Program: Running Total
# This program asks users for 5 numbers
# It then sums up the products


sum = 0
how_many_numbers = int(input('\nHow many numbers would you like to sum up: '))
print('')
for i in range(how_many_numbers):
    enter_a_number = int(input('Enter a Number: '))
    sum = sum + enter_a_number

print('\nThe sum of your numbers is: ' + str(sum))


# Programmer: Elle Green
# Date: 1-7-20
# Program: Average Test Scores
# This program asks users how many tests they will average


total = 0
how_many_tests = int(input('\nHow many tests would you like to average: '))
print('')
for i in range(how_many_tests):
    enter_a_score = float(input('What was the score you got on your test: '))
    total = total + enter_a_score

average = total / how_many_tests
print('Your finale average test score is: ' + str(round(average, 2)))

print('\nThis class is very fun, but I wish we had more than just every friday to work on our R&D projects')
print('I feel like if we worked on that more then kids would be more excited for the end of each week')
print('We could make thursdays every other week and every fridays R&D days.This would give people more time to figure-')
print('things out and make there program or app or whatever they are working on more complex and easier to use.\n')


# Date: 1-20-20
# Program: Double For Loop

for i in range(3):
    print("Outer For Loop " + str(i))
    for k in range(4):
        print("\tInner for Loop " + str(k))


"""
Programmer: Elle Green
Date: 1-23-20
Program: While Loop nested inside of a For Loop
"""
print("\n**********************\n")
for i in range(4):
    print("For Loop " + str(i))
    x = i
    while x >= 0:
        print("\tWhile Loop" + str(x))
        x = x-1
        

# Programmer Elle Green
# Date 2-3-20

# Declare Global Variables
name = input('\nWhat is your name: ')
x = 15



# Create Functions here

# Greeting Function
def greeting():
    print('Hi there ' + name)
    print(x)

# Functions and Local Variable x
def printSomething():
    x = 3
    print(x)

# Functions and Parameters
def printNumber(age):  # function name = printNumber, parameter = age
    print(age)

# Default Parameter values

def printTwoNumbers(x, y = 71):
    print("First Parameter(Number): " + str(x))
    print("Second Parameter(Number): " + str(y))

# Print Sum
def printSum(x, y):
    print(x + y)

# Print Multiple Times
def printMultiTimes(string, times):
    for i in range(times):
        print(string)


# Call Functions here
print("\n******Greetings Function*******\n")
greeting()

print("\n******Print Something Function*******\n")
printSomething()

print("\n******Print Number Function*******\n")
printNumber(28)
printNumber(24)

print("\n******Print 2 Numbers Function*******\n")
printTwoNumbers(23, 78)
printTwoNumbers(45)

print("\n******Print Sum Function*******\n")
printSum(45, 56)

print("\n******Print Multiple Times Function*******\n")
printMultiTimes("I love computer science", 7)
