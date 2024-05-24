class Grandfather:
    def __init__(self) -> None:
        print('grandfather owns a luxury house')
    house = 'luxury house'
    
class Father(Grandfather):
    def __init__(self) -> None:
        super().__init__()
        print('father bought a luxury house')
    car = 'Ferrari'
    
class Mother:
    jewellery = 'gold'
    
class Son(Father,Mother):
    console = 'PS5'
    
son=Son()
print(son.house)
print(son.car)
print(son.jewellery)
print(son.console)