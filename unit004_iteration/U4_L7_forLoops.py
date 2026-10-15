'''
Created on Oct 15, 2026

@author: ogracias
'''
for jacob in range(5):# iterator
    print(jacob,': Hello')

for i in range(1, 11):
    print(i, end=" ")

print()
for i in range(1, 15, 3):
    print(i)

print()
for i in range(40, 4, -8):
    print(i)
import random


same_side_counter = 0
n = int(input('How any coin tosses? '))
for i in range(1, n + 1):
    print('toss #' + str(i))
    coin_1 = random.randint(0, 1)
    print('coin1:', coin_1)
    coin_2 = random.randint(0, 1)
    print('coin2:', coin_2)
    print()
    if(coin_1 == coin_2):
        same_side_counter += 1
print('Coins were the same', same_side_counter, 'times.')
    
country = 'United States of America'
for letter in country:  
    if letter.isupper():
        print(letter)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









