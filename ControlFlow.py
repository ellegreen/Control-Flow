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
