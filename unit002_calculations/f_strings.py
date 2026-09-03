'''
Created on Sep 3, 2026

@author: ogracias
'''
print('****************')
print("data types in print")
print('****************')
'''
s --> string
d --> integers
e --> exponents
f --> fixed-point notation.
'''
variable = 1_045_634
print(f'Using numeric value {variable = }')
print(f'This prints without formatting {variable}')
print(f'This prints with formatting {variable:d}')
print(f'This prints with spacing {variable:10}')
print(f'This prints with exponents {variable:e}')



print('****************')
print("floats")
print('****************')
pi = 3.141592653589
print(f'Using the value of pi = {pi}')
print(f'|{pi:>25}|')
print(f'|{pi:<25}|')
print(f'|{pi:^25}|')


floatVariable = 1_045_634.64656465
print(f'without formatting {floatVariable =}')
print(f'with commas {floatVariable:,f}')
print(f'with commas {floatVariable:,.2f}')


print('****************')
print("tabbing")
print('****************')
first = 'Monday'
second = 'Tuesday'
third = 'Wednesday'
meal1 = 'tacos'
meal2 = 'soup'
meal3 = 'beef'
print(f'|{first:^10s}|{second:^10s}|{third:^10s}|')
print(f'|{meal1:^10s}|{meal2:^10s}|{meal3:^10s}|')









