# Date 2-3-20
# Greeting Function

# Declare Global Variables
name = input('\nWhat is your name: ')
x = 15

# Create Functions here
def greeting():
    print('Hi there ' + name)
    print(x)

def printSomething():
    x = 3
    print(x)

# Call Functions here
greeting()
printSomething()
print(x)