import unittest

# Collatz sequence problem
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(number * 3 + 1)
        return number * 3 + 1

print('Enter number:')

validInput = False

while not validInput:
    try:
        inputNumber = int(input())

        while inputNumber != 1:
            inputNumber = collatz(inputNumber)

        validInput = True
    except ValueError:
        print('Please enter a non-negative integer value:')