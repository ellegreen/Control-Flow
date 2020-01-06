"""
Programmer: Elle green
Date: 1-6-20
Program: Running Total

This program asks users for 5 numbers
It then sums up the products
"""

sum = 0

for i in range(5):
    enter_a_number = int(input('Enter a Number: '))
    sum = sum + enter_a_number

print('\nThe sum of your numbers is: ' + str(sum))
