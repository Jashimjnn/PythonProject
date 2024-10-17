from Menu import Menu
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.menu = Menu()
    
    def add_users(self, employee):
        self.employees.append(employee)

    def view_users(self):
        print("Employee list")
        for em in self.employees:
            print(em.name, em.phone, em.email, em.address)