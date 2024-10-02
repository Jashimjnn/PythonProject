#Ena poribohon
class Company:
    def __inti__(self,name,address)->None:
        self.name = name
        self.bus = []
        self.routers = []
        self.driver = []
        self.counter = []
        self.manager = []
        self.supervisor = []
        self.fare = []

class Driver:
    def __inti__(self,name,licence,age)->None:
        self.name = name
        self.licence = licence
        self.age = age
class Counter:
    def __init__(self)->str:
        pass
    def purches_ticket(self,start,destination):
        pass
class Passenger:
    pass
class Supervisor:
    pass