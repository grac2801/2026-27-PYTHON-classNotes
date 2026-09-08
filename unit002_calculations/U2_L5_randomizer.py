'''
Created on Sep 8, 2026

@author: ogracias
'''
import random

#print a random value between 0 and < 1
print(random.random())


# I want to print a random value between 1 and 5
print(f'The random number is', random.randint(1, 5))
print(f'The random number is {random.randint(1, 5)}')
print(int(random.random() * 5) + 1)


print(random.choice(['Jacob', 'Jose', 'Mateo', 'Jordan']))

'''
Write a program to generate a unique password
requirements =
1) number 1 - 100 inclusive
2) an animal from a list of 5 animals
3) another number between 4 - 10
print the password
'''
myList = ['hen', 'mouse', 'elephant', 'dog', 'cat']
num1 = str(random.randint(1, 100))
animal = random.choice(myList)
num2 = str(random.randint(4, 10))
pw = num1 + animal + num2
print('My password is ' + pw)



#===============================================================================
# randrange
#===============================================================================
# print only even numbers from 2 to 10
# randrange(start, end [not inclusive], step)
print(random.randrange(2, 11, 2))

# Only numbers divisible by 4 from 4 to 40
print(random.randrange(4, 41, 4))


# get a specific number of items from a list
fruits = ['grapes', 'oranges', 'apples', 'pears', 'figs', 'bananas']
print(f'Original list of fruits: {fruits}')
newList = random.sample(fruits, k = 3)
print(f'My new 3-item list: {newList} ')

'''
Mimic the toss of 2 dice, and add the values
'''
first_toss = random.randint(1, 6)
second_toss = random.randint(1, 6)
total = first_toss + second_toss
print(f"The total toss value is {total}")


