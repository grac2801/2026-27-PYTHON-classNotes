'''
Created on Sep 17, 2026

@author: ogracias
'''
import random

# print('****************')
# print("#1 while loop")
# print('****************')
# num = 1 # 1. declaring and initializing a variable
# while num <= 5: # 2. condition
#     print(num, 'Hello')
#     num += 1 #3, move the variable forward
#
#
# print('****************')
# print("#2. Sentinel value")
# print('****************')
# num = int(input('Enter a number, -1 to stop: '))
# while(num != -1):
#     print('You entered: ' + str(num))
#     num = int(input('Enter another number, -1 to stop: '))
# print('Done')
#
#
#
# print('****************')
# print("3. Loops and strings")
# print('****************')
# name = input('Enter a name: ')
# while name != 'Ada':
#     print('Hmm..' + name + ' is an interesting name!')
#     name = input('Enter a name: ')
# print('Cool - That is my name too')
    
print('****************')
print("Coding activity")
print('****************')
'''
Create an algorithm that provides 3 attempts to guess a password.
If it is found, you should display "Welcome to the portal".
Else, "Wrong password, try again". Once all 3 attempts are used,
you will display: "Call the FBI"
'''
print('Hello user, Welcome to the portal: ')
pw = 'swordfish'
guess = input('Enter password: ')
attempts = 1
while(guess != pw):
    print('attempt #', attempts)
    if(attempts >= 3):
        print('Call the FBI')
        break
    print('Wrong password, try again')
    attempts += 1
    guess = input('Enter password: ')
else:
    print('Welcome to the portal')  
    
print('****************')
print("print 10 random numbers between 1 and 10")
print('****************')
counter = 0
while(counter < 10):
    number = random.randint(1, 10)
    print('number:', number)
    counter += 1

























