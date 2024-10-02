class vehicle:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price
    def __repr__(self) -> str:
        return f'{self.name} {self.price}'
    
class Bus(vehicle):
    def __init__(self,name,price,seat)-> None:
        self.seat = seat
        super().__init__(name,price)
    def __repr__(self) -> str:
        return super().__repr__()
class Truck(vehicle):
    def __init__(self,name,price,weight)-> None:
        self.weight = weight
        super().__init__(name,price)
    def __repr__(self) -> str:
        return super().__repr__()
class PickupTruck(Truck):
    def __init__(self,name,price,weight)-> None:
        super().__init__(name,price,weight)
    def __repr__(self) -> str:
        return super().__repr__()
class ACBus(Bus):
    def __init__(self,name,price,seat,temparature) -> None:
        self.temparature = temparature
        super().__init__(name,price,seat)
    def __repr__(self) -> str:
        return super().__repr__()
    
green_line  = ACBus('Green',2000000,22,25)
print(green_line)
Blue_line  = PickupTruck('Blue',500000,22)
print(Blue_line)