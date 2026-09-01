'''
Created on Aug 28, 2026

@author: ogracias
'''
# Ask a question
name = input('What is your name? ')
# The answer is saved as a string
print('Good morning!', name, '.Nice to meet you')
print('\n\n')
#Adding 2 numbers
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
total = num1 + num2
print('The total is', total)

'''
Variable name rules.
1. They can be letters and numbers, but no spaces
2. They have to start with a lowercase
3. They can not start with a number (i.e 12day)
4. Use descriptive names
5. camel case or underscores are OK for multiple
   words
   [daysOfTheWeek, days_of_the_week]
'''



'''
Student activity
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that 
they will turn 100 years old.
'''
myName = input('What is your name? ')
age = int(input('Enter your age: '))
year = 2026 - age + 100
print(myName, '. You will be 100 years old in the year: ', str(year))
















