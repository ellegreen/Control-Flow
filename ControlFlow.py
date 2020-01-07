"""
Programmer: Elle green
Date: 1-6-20
Program: Running Total

This program asks users for 5 numbers
It then sums up the products
"""

sum = 0
how_many_numbers = int(input('How many numbers would you like to sum up: '))
print('')
for i in range(how_many_numbers):
    enter_a_number = int(input('Enter a Number: '))
    sum = sum + enter_a_number

print('\nThe sum of your numbers is: ' + str(sum))
