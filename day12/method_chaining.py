class Burger:
    
    def bun(self):
        print('bun')
        return self
    
    def patty(self):
        print('patty')
        return self
    
    def tomato(self):
        print('tomato')
        return self
    
    def cheese(self):
        print('cheese')
        return self

b=Burger()
b.bun().patty().patty().tomato().cheese().cheese().cheese().cheese().bun()