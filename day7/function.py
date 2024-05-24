# def hello(name):
#     print(f"hello {name}, k gardai chhau??")
          
# hello("Ram")
# hello('Shyam')
    
# def person(name, age, gender):
#     print(f"My name is {name}")
#     print(f"I am {age} years old")
#     print(f"I am {gender}")
# person(age=12,gender="male",name="Ram")

# def sum(*numbers): # * represents arguments (args)
#     total=0
#     for number in numbers:
#         total+=number
#     print(total)
    
# sum(1,2,3,4)

# def person(**attrs):
#     print(f"my name is {attrs['name']}")
#     print(f"my age is {attrs['age']}")
#     print(f"my gender is {attrs['gender']}")
#     print(f"my surname is {attrs['surname']}")
    
# person(age=12,name="JOhn",gender="male",surname="thapa")

# # recurssion
def number(i=0):
    print(i)
    if i==10:
        return
    number(i+1)
    
number()
    