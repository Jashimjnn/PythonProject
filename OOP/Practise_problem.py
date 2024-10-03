class Product:
    def __init__(self,name,price,quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
    def __repr__(self) -> str:
        print('I love Bangladesh')
class Shop:
    def __init__(self) -> None:
        self.product = []
    def add_product(self,name):
        self.product.append(name)
    def buy_product(self,pr_name):
        for item in self.product:
            if item.name == pr_name:
                if item.quantity>0:
                    item.quantity-=1
                    print('Congratulation! Here your product')
                    return
                else:
                    print('Sorry! you cannot buy')
        print(f'{pr_name} is not available')
sh = Shop()

p1 = Product('Laptop',500000,5)
p2 = Product('Mobile',80000,8)

sh.add_product(p1)
sh.add_product(p2)

sh.buy_product('Laptop')
sh.buy_product('Tablet')
sh.buy_product('Mobile')