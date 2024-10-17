from Order import Orders
class Users:
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone  = phone
        self.email = email
        self.address = address


class Customaer(Users):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Orders()
    
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self,restaurant,item_name,quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item Exceeded !")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item added")
        else:
            print("Item not found")

    def view_cart(self):
        print("*****View cart*****")
        print("Name\tPrice\tQuantity")
        for item,qunatity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{qunatity}")
        print(f"Total Price : {self.cart.total_price()}")

    def paybill(self):
        print(f"Total {self.cart.total_price()} paid successfully !")
        self.cart.clear()


class Admin(Users):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees = []

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def delete_item(self, restaurant, item):
        restaurant.menu.remove_item(item)
    
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()


class Employee(Users):
    def __init__(self, name, phone, email, address, age, designation, salary):
        self.age = age
        self.designation = designation
        self.salary = salary
        super().__init__(name, phone, email, address)