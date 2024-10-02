class Shopping:

    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self,amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        print('Total : ',total)
        if amount<total:
            print(f'Provide money : {total-amount}')
        else:
            extra = amount-total
            print(f'Here your money {extra}')

swapan = Shopping('Alan')
swapan.add_cart('alu',50,6)
swapan.add_cart('dim',12,24)
swapan.add_cart('rice',50,5)
print(swapan.cart)
swapan.checkout(1600)