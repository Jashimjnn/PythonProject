from Order import Order
class Users:
    def __init__(self,email,password):
        self.email = email
        self.password = password
    

class Customer(Users):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.cart = Order()
    
    def view_menu(self,shop):
        shop.menu.show_menu()
    
    def add_to_cart(self,shop,item_name,quantity):
        item = shop.menu.find_item(item_name)
        if item:
            if quantity>item.quantity:
                print(f"Item quantity Exceeded !")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item added")
        else :
            print("Item not found")
    

    def view_cart(self):
        print("*****View Cart*****")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price: {self.cart.total_price()}")
    
    def paybill(self):
        print(f"Total Price: {self.cart.total_price()} paid Successfully!")
        self.cart.clear()


class Sellers(Users):
    def __init__(self, email, password):
        super().__init__(email, password)

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def delete_item(self, restaurant, item):
        restaurant.menu.remove_item(item)
    
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()
    
    def add_users(self, restaurant, employee):
        restaurant.add_users(employee)

    def view_users(self, restaurant):
        restaurant.view_users()


class Employee(Users):
    def __init__(self,email,password):
        self.email = email
        self.password = password






