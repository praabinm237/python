while True:
    try:
        a = int(input('Enter a number : '))
        b = int(input('Enter a number : '))
        
        if a==5:
            raise Exception('5 is invalid number!!')
        print(a/b)
        
    except ZeroDivisionError:
        print('Any number divided by zero is infinite')
    
    except ValueError:
        print('number can only be integer')
        
    except Exception as e:
        print(f'error ayo {e}')