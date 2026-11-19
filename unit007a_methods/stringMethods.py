# ogracias
# 2026-11-12
# TOPIC: String methods

# imports




# functions
def capitalize():
    word = input('Enter a word using lower case: ')
    print('original word:', word)
    word = word.capitalize()
    print('capitalized: ',word)


def count():
    '''
    counts the instances of a string in another string
    '''
    myString = input('Enter a string \u2192 ')
    search_item = input('What string are you looking for? ')
    print('Your string:', myString)
    print('Searching:', search_item)
    numTotal_a = myString.count(search_item)
    print('total times found:', numTotal_a)
    return numTotal_a

def endswith():
    '''
    Check if the string ends with a punctuation sign
    str --> boolean
    "Hello, welcome to my world.".endswith(".") --> True
    '''
    myString = input('Enter a string \u2192 ')
    lastChar = input('Enter last character in question: ')
    answer = myString.endswith(lastChar)
    return answer
if __name__ == '__main__':
    topic = 'String functions'
    print(topic.center(80, '*'))
    print(f"")
    go_on = True
    while go_on:
        print(f"{'1. capitalize':<30s}{'12. lstrip':<30s}{'23. casefold()':<30s}")
        print(f"{'2. count()':<30s}{'13. replace(old,new,max)':<30s}{'24. expandtabs()':<30s}")
        print(f"{'3. endswith()':<30s}{'14. rstrip()':<30s}{'25. isalnum()':<30s}")
        print(f"{'4. find(s)':<30s}{'15. rstrip(s)':<30s}{'26. isalpha()':<30s}")
        print(f"{'5. find(s, beg)':<30s}{'16. split()':<30s}{'27. index()':<30s}")
        print(f"{'6. find(s, beg, end)':<30s}{'17. startswith(beg)':<30s}{'28. isdecimal()':<30s}")
        print(f"{'7. format()':<30s}{'18. strip()':<30s}{'29. isdigit()':<30s}")
        print(f"{'8. isLower()':<30s}{'19. zfill()':<30s}{'30. ididentifier()':<30s}")
        print(f"{'9. isUpper()':<30s}{'20. swapcase()':<30s}{'31. isprintable()':<30s}")
        print(f"{'10.lower()':<30s}{'21. upper()':<30s}{'32. isspace()':<30s}")
        print(f"{'11.lstrip()':<30s}{'22. title()':<30s}{'33. istitle()':<30s}")
        
        number = int(input('\n\nWhat number method do you wish more info about? '))
        if number == 1:
            capitalize()            
        go_on = input('Do you with to continue? (y | n)')
        go_on = go_on.capitalize()
        
        
        
        # iterate back up
        if go_on == 'Y':
            go_on = True
        else:
            go_on = False
        

    
    
    
    
    
    
    
    