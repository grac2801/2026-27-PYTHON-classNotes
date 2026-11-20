# ogracias
# 2026-10-23
# TOPIC: Functions with returns

# imports
import math
import random


# functions
def addition(a, b):
    return a + b

def multiply(x, y):
    answer = x * y
    return answer

def pythagorean_SolveC(a, b):
    a_squared = math.pow(a, 2)
    b_squared = math.pow(b, 2)
    c_squared = math.sqrt(a_squared + b_squared)
    return c_squared

def randomCard():
    card_total = 0
    num = random.randrange(1, 12)
    card_total += num
    suits = ['hearts', 'spades', 'diamonds', 'clubs']
    suit = random.choice(suits)
    if num == 1:
        num = 'Ace'
    return str(num) + ' of ' + suit
    
    

if __name__ == '__main__':
    print(randomCard())

    print(addition(23, 87))
    print(multiply(6, 3))
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    
    print(pythagorean_SolveC(a, b))



    
    
    