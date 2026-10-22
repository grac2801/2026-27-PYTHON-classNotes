# ogracias
# 2026-10-22
# TOPIC: Use of parameters

# imports




# functions
def name0(n) -> None:
    print('Nice to meet you ' + n)

def name1(fn, ln, age):
    print('Nice to meet you ' + fn)
    print(ln + ' is a cool last name.')
    if(age >= 21):
        print('You are old enough to vote.')
    else:
        print('You are too young to vote')
        
def name2(fn, ln, age = 16):
    print('Nice to meet you ' + fn)
    print(ln + ' is a cool last name.')
    print('Your age is: ', age)

if __name__ == '__main__':
    # name0('Mr. Gracias')
    # name1('Oscar', 'Gracias', 55)
    firstName = input('Enter your first name: ')
    lastName = input('Enter your last name: ')
    myAge = int(input('Enter your age: '))
    name2(firstName, lastName, myAge)
    
    
    
    
    
    
    
    
    
    