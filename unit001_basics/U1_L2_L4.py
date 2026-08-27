'''
Created on Aug 27, 2026

@author: ogracias
'''
print('Learning to print')
# Default separator
print('Hello', 'Mr', 'Gracias')
print('Hello ' + "Mr." + 'Gracias')

# ctrl + alt + arrow down --> copy down a line
# ctrl + alt + arrow up --> copy up a line
# alt + arrow down --> move the line down

# separator and end parameters
print('Hello', 'Mr', 'Gracias')

# Explicit separator
print('Hello', "Mr.", "Gracias", sep=' * ', end='\n')
print('my next line')

# variables
firstNumber = 5
secondNumber = 10

# print variables
print(firstNumber)
print(secondNumber)

# modified print
print(firstNumber, end=' and ')
print(secondNumber)

# formatting output
myAge = 55
favoriteColor = 'dark blue'

print('I am {0} years old, and my favorite color is {1}'.format(myAge, favoriteColor))
print('I am {1} years old, and my favorite color is {0}'.format(myAge, favoriteColor))

# new formatting
print(f'I am {myAge} years old. My favorite color is: {favoriteColor}')

print('\n\n***Concatenation***')
print('Hello my dear' + 'Mary')
# to fix
print('Hello my dear ' + 'Mary')
print('Hello my dear' + ' Mary')

print("look here")



















