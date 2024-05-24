total = 0
def deposit():
    global total
    amount=float(input('\nEnter any amount : '))
    total+=amount
    print(f'You\'ve successfully deposited Rs. {amount} to your account')

def withdraw():
    global total
    amount=float(input('\nEnter any amount : '))
    if amount>total:
        print('Insufficient balance')
    else:
        total-=amount
        print(f'You\'ve successfully withdrawn Rs. {amount} from your account')
    
def balance():
    print(f'Your total balance is Rs. {total}')
  
    
def main():
    account=input('Press 1 to create an account : ')
    if account=='1':
        username=input('Enter new username : ')
        passcode=int(input('Enter new passcode : '))
        print('Account created successfully\n')
    else:
        print('Invalid input')
        return main()
    db={'name':username, 'pass':passcode}
    
    def Login():
        login=input('Press 1 to continue \n')
        if login=='1':
            print('Welcome to Login Page')
            username1=input('Enter your name : ')
            pass1=int(input('Enter your passcode : '))

            if db['name']==username1 and db['pass']==pass1:
                def interface():
                    while True:
                        print('\nWelcome to ABC bank')
                        print('Press 1 to deposit')
                        print('Press 2 to withdraw')
                        print('Press 3 to check the balance')
                        print('Press 4 to exit')
                        option=input()
                        if option=='1':
                            deposit()
                        elif option=='2':
                            withdraw()
                        elif option=='3':
                            balance()
                        elif option=='4':
                            print('Exited successfully')
                            break
                            
                        else:
                            print('Invalid input')
                            
                interface()
            else:
                print('Invalid name or passcode\n') 
                return Login()
                    
        else:
            print('Invalid input')
            return Login()
    Login()                
            
            
main()

    