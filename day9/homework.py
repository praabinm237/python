def number(i=1):
    if i>=10:
        return
    print(i)
    number(i+2)
    
number()