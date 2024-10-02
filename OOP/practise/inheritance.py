class gadget:
    def __init__(self,name,brand,price,color) -> None:
        self.name = name
        self.brand = brand
        self.price = price
        self.color = color
class laptop(gadget):
    def __int__(self,name,brand,price,color):
        super().__init__(name,brand,price,color)
    def __repr__(self) -> str:
        return f'Laptop : {self.name} {self.brand} {self.price} {self.color}'

class mobile(gadget):
    def __init__(self,name,brand,price,color):
        super().__init__(name,brand,price,color)
    def __repr__(self) -> str:
        print(f'Laptop : {self.name} {self.brand} {self.price} {self.color}')

my_laptop = laptop('Laptop','HP',200000,'Blue')
print(my_laptop)