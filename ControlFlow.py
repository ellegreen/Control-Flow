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


"""
Programmer: Elle Green
Date: 1-7-20
Program: Average Test Scores

This program asks users how many tests they will average
"""

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
print('things out and make there program or app or whatever they are working on more complex and easier to use. ')
