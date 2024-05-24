a=int(input('Enter first number :'))
b=int(input('Enter second number :'))

# ctrl+D : same variable lai ekai choti change garna paryo ki
# ctrl+Alt+down/up arrow  : ekai choti multiple line ma lekhna paryo ki

o=input('Enter the operator +,-,*,/ :')

if o=='+':
    print('The sum is :', a+b)
elif o=='-':
    print('The subtraction is :', a-b)
elif o=='*':
    print('The multiplication is :', a*b)
elif o=='/':
    if b==0:
        print('Any number divided by 0 is infinity')
    else:
        print('The division is :', a/b)
else:
    print('unsupported operator')
    
#user input number
#multiplication table
#odd or even number


