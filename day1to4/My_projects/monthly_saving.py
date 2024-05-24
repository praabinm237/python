name=input('Enter your name : ')

def monthly_saving():
    
    month=input('Enter month\'s name : ')
    a=int(input(f'Enter total days of {month} : '))

    total = 0
    for a in range(1,a+1):
        total+=a
        
    print(f'Dear {name}, you have to save Rs. {total} for the month of {month}')
    print('                      **********************                         ')
    if month=='December':
        return
    return monthly_saving()
    
monthly_saving()

