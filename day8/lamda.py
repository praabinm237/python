# def sum(a,b):
#     return a+b
# sum=lambda a,b:a+b

# print(sum(1,2))

def fuc(n):
    return lambda x:x*n

# lambda x:x*2
doubler=fuc(2)
# tripler=fuc(3)

print(doubler(2))