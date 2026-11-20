# ogracias
# 2026-11-19
# TOPIC: loops and lists

# imports
import random



# functions




if __name__ == '__main__':
    print('****************')
    print("1.Make a list of 10 numbers between 1-25")
    print('****************')
    luckyNumbers = []
    for i in range(10):
        luckyNumbers.append(random.randint(1, 25))
    print(luckyNumbers)
    
    
    print('print i and values using the len (length)')
    for i in range(0, len(luckyNumbers)):
        print(luckyNumbers[i])
    for i in range(0, len(luckyNumbers)):
        print(i)
        
        
    print('****************')
    print("Another way to print a list")
    print('****************')
    for number in luckyNumbers:
        print(number)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    