def hash(func):
    def wrapper():
        print("#"*10)
        func()
        print("#"*10)
    return wrapper

def star(func):
    def wrapper():
        print("*"*10)
        func()
        print("*"*10)
    return wrapper

@hash
@star
def hello():
    print("Hello")
    
@hash
@star
def bye():
    print("bye")
    
hello()
bye()