# a=10

# def hello():
#     # global a
#     a=11
#     print(a)
    
# hello()
# print(a)

x=9

def outer():
    def inner():
        print(f'inner sees x as {x}')
    inner()
    print(f'outer sees x as {x}')
    
outer()
print(f'global sees x as {x}')


# recursion -> fibanaci print

# list(range(1,10,2)) -> recurssion recreate

# # people=[
#     {
#         'name':'John',
#         'age' : 30,
#         'gender' : 'male'
#     }
# ]