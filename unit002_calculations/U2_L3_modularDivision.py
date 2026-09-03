'''
Created on Sep 3, 2026

@author: ogracias
'''
print('When 10 is divided by 3, the remainder is:', 10 % 3)

# user input
firstValue = int(input('Enter first value: '))
secondValue = int(input('Enter second value: '))
print('The remainder is: ', firstValue % secondValue)


print('****************')
print("Example")
print('****************')
# Modulus is used for repetition or patters.
# Example: when using time
totalMinutes = int(input('How may minutes are you converting?'))
hours = int(totalMinutes / 60)
minutesRemaining = totalMinutes % 60
print(f'There are {hours:d} hour(s), \
and {minutesRemaining:d} minute(s) in {totalMinutes:d} minutes')







