class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
        print('vat mangso polau korma')
class Cricket(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)
    
    #Overridding
    def eat(self):
        print('Vagetable')

    #Over Loading
    def __add__(self,other):
        return self.age+other.age
    def __mul__(self,other):
        return self.weight*other.weight
    def __len__(self):
        return self.height
    def __gt__(self,other):
        return self.height>other.height
    def __le__(self,other):
        return self.height>other.height

sk = Cricket('Sakib',38,68,91,'BD')
mushi = Cricket('mushi',36,65,78,'BD')
#sk.eat()

print(sk+mushi)
print(sk*mushi)
print(len(sk))
print(sk>mushi)
print(sk<mushi)