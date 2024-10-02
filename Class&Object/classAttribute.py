class Shop:

    cart = []

    def __init__(self,buyer):
        self.buyer = buyer
    def add_to_cart(self,product):
        self.cart.append(product)

Mehjabeen = Shop("Meh jabeen")
Mehjabeen.add_to_cart("shoe")
Mehjabeen.add_to_cart("tops")
Mehjabeen.add_to_cart("chury")
print("Mehjabeen : ",Mehjabeen.cart)

Nisho = Shop("Nisho")
Nisho.add_to_cart("watch")
Nisho.add_to_cart("cap")
Nisho.add_to_cart("t-shirt")
print("Nisho : ",Nisho.cart)