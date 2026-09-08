'''
Created on Sep 8, 2026

@author: ogracias
'''

print('==================================================')
print('TOPIC: -->', '1. simple ifs' )
print('==================================================')
# value = int(input('Enter a number: '))
# if value > 0:
#     print('positive value')
# print('Done')

print('\n\n')
print('==================================================')
print('TOPIC: -->', '2. Another if example' )
print('==================================================')
sunny = True
if sunny:
    print('I do not need an umbrella.')
if not sunny:
    print('I DO need an umbrella')
    
print('\n\n')
print('==================================================')
print('TOPIC: -->', '3. odd or even' )
print('==================================================')
number = int(input('Enter a number: '))
# check if even or odd
if number % 2 == 0:
    print(str(number) + ' is even')
if number % 2 == 1:
    print(str(number) + ' is odd')
if number % 2 == 0 or number % 3 == 0:
    print(str(number) + ' is divisible by 2 or 3')




























