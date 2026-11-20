'''
Created on Oct 15, 2026

@author: ogracias
'''
import random
print('****************')
print("Which loop to user to print python 10 times")
print('****************')
count = 1
while(count <= 10):
    print(f"{count:4}: Python")
    count+= 1


print('****************')
print("Ask user for 5 numbers and add numbers divisible by 3")
print('****************')
counter = 0
totalSum  = 0

while(counter < 5):
    n = int(input('Enter a number: '))
    if(n % 3 == 0):
        print(n, 'is divisible by 3')
        totalSum += n
    counter += 1
print("The total sum of numbers divisible by 3 is: " + str(totalSum))


print('****************')
print("User input, but number of iterations unknown")
print('****************')
# Ask user to input a number until that number is > 100
numGreater_100 = int(input('Enter a number: '))
while(numGreater_100 <= 100):
    numGreater_100 = int(input("Enter a number: "))


print('****************')
print("Enter numbers and get an average [Use of sentinel value: -1]")
print('****************')
counter = 0
addition = 0

n = int(input('Enter an integer (-1 to end)'))
if n == -1:
    print('-1 was input. Script ends now.')
else:
    while(n != -1):
        counter += 1
        addition += n
        n = int(input('Enter an integer (-1 to end)'))
    average = (addition / counter)
    print(f'The average is:', average)
print('Done')
    
print('****************')
print("unicode symbols")
print('****************')
clockwiseArrow = '\u21BB'
print(clockwiseArrow)
triangularArrow = '\u27A4'
print(triangularArrow)
anchor = '\u2693'
print(anchor)

c = 0
while(c < 5):
    value = random.randint(0, 2)
    
    if(value == 0):
        print('Clockwise arrow:', clockwiseArrow)
        c += 1
    elif(value == 1):
        print('triangular arrow:', triangularArrow)
        c += 1
    elif(value == 2):
        print('anchor:', anchor)
        c += 1





























