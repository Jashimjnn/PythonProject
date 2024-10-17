from Menu import Menu
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee list")
        for em in self.employees:
            print(em.name, em.phone, em.email, em.address)