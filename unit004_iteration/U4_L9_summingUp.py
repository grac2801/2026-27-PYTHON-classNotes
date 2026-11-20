'''
Created on Oct 20, 2026

@author: ogracias
'''
#imports 



# functions



if __name__ == '__main__':
    print('****************')
    print("summing values")
    print('****************')
    total = 0
    for i in range(34, 68):
        total += i
        print(f"{i}= {total:,}")
    
    
    print('****************')
    print("Add all even numbers")
    print('****************')
    # Add all even numbers starting at 2 and ending at
    # 100 using the for loop
    total = 0
    for i in range(2, 101, 2):
        total += i
    print(f"The sum of all evens is: {total:,}")
    
    
    # print('****************')
    # print("Adding user input")
    # print('****************')
    # # Ask for 5 numbers, add them, and show the total
    # total = 0
    # for i in range(5):
    #     n = int(input('Enter a number\u2192 '))
    #     total += n
    # print(f'The sum is: {total:,}')
    
    print('****************')
    print("user input, taxes, and total")
    print('****************')
    total = 0
    times = int(input('How many items do you need? '))
    for i in range(times):
        cost = float(input('How much does the item ' + str(i + 1) + ' cost?'))
        total += cost
    print(f'Total: ${total:,.2f}')
    taxes = total * 0.0875
    print(f'taxes: ${taxes:,.2f}')
    total = total + taxes
    print(f'Total owed: ${total:,.2f}')
    
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







