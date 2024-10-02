class Phone:
    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price
    
my_phone = Phone('Jashim','Samsung',20000)
print(my_phone.owner,my_phone.brand,my_phone.price)