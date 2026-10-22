# ogracias
# 2026-10-22
# TOPIC: Introduction to functions

# imports
import random



# functions
def printSomething() -> None:
    print('This is my first function')


def flipCoin() -> None:
    outcome = random.randint(0, 1)
    if outcome == 0:
        print('tails')
    else:
        print('heads')    


def lovePython() -> None:
    print('I \u2661 Python')

if __name__ == '__main__':
    # flipCoin() 
    for i in  range(3):   
        lovePython()
    
    
    
    
    
    
    
    
    
    