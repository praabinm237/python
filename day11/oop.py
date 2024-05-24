# class House:
    
    
#     def __init__(self,window=5,color='black'):
#         self.window=window
#         self.color=color
        
#     def __str__(self) -> str:
#         return f'{self.window} {self.color}'
    
#     def __eq__(self, obj):
#         return self.window==obj.window
    
#     # method
#     def hello(self,name):
#         print(f'Hello {name}')
    
# ram_ko_ghar=House(color='red')
# # ram_ko_ghar.hello('Ram')
# print(ram_ko_ghar.color)
# print(ram_ko_ghar.window)

# shyam_ko_ghar=House()
# print(shyam_ko_ghar.color)

class Person:
    def __init__(self, name, age, password):
        self.name = name
        self._age = age # protected variable
        self.__password = password # private variable
        
    def __str__(self) -> str:
        return f'{self.name} {self.age} {self.password}'
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password
        
ram = Person('ram', 12, '123')
ram.password = "passwd"
print(ram.password)