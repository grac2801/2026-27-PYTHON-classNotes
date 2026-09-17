'''
Created on Sep 15, 2026

@author: ogracias
'''
print('----- if statements-------')
myComment = '''
pH level          Category
0 - 4             Strong acid
5 - 6             Weak acid
7                 Neutral
8 - 9             weak base
10 - 14           Strong base
'''
print(myComment)
pH = float(input('Enter the pH value: '))
if pH < 7.0:
    print('It is acidic')
    print('You should be careful with that')
if pH > 7:
    print("It is basic")
if pH == 7:
    print('It is neutral')



# it will print incorrect data
grade = float(input('Enter your percent grade: '))
if grade > 90:
    print('You have an A')
if grade > 80:
    print('You have an B')
if grade > 70:
    print('You have an C')
if grade > 60:
    print('You have an D')
else:
    print('you failed.')
    
    
grade = float(input('Enter your percent grade: '))
if grade > 90:
    print('You have an A')
elif grade > 80:
    print('You have an B')
elif grade > 70:
    print('You have an C')
elif grade > 60:
    print('You have an D')
else:
    print('you failed.')


print('****************')
print("Nested if statements")
print('****************')
value = float(input('Enter the pH value: '))
if value > 0:
    if value < 7.0:
        print('it is acidic')
    elif value > 7 and value <= 14:
        print('It is basic')
    elif value == 7:
        print('It is neutral')
elif value > -10:
    print('You input a negative pH value')
else:
    print('less than -10')

print('****************')
print("unicodes")
print('****************')
compound = input('Enter the compound: ')
if(compound == 'H2O') or (compound == 'h2o'):
    print('H\u2082O')
elif compound == 'NH3':
    print('NH\u2083')
elif compound == 'CH4':
    print('methane')
else:
    print('I do not know which compound this  is')










