# ogracias
# 2026-11-19
# TOPIC: Searching algorithm

# imports




# functions
def printIt(a):
    for i in range(len(a)):
        print(a[i])


def findIt(a, e):
    for i in range(len(a)):
        if (a[i] == e):
            return 'Found at index:', i
    return 'Not found'

if __name__ == '__main__':
    print('****************')
    print("find an item in an array")
    print('****************')
    words = ['asphalt', 'assignment', 'asterisk', 'attorneys', 'audible', 'aviator']
    printIt(words)
    
    word = input('Enter the word you are looking for: ')
    print(findIt(words, word))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    