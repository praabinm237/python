from abc import ABC, abstractmethod

class Computer(ABC):
     @abstractmethod
     def process(self, app):
         pass
     
     def run(self, app):
         return self.process(app)
     
class Laptop(Computer):
    
    def process(self, app):
        print(f'Laptop is running {app}')
        
dell = Laptop()
dell.run('pubg')

class Mobile(Computer):
    
    def process(self, app):
        print(f'Mobile is running {app}')
        
iphone = Mobile()
iphone.run('Call of Duty')
         