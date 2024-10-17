from Food_Item import FoodItem
from Order import Order
from Menu import Menu
from Restaurant import Restaurant
from users import Customer,Admin,Employee

mamar_res = Restaurant("Mamar Restaurant")
def customer_menu():
    name = input("Enter Your Name : ")
    Phone = int(input("Enter Your Phone : "))
    Email = input("Enter Your Email : ")
    Address = input("Enter Your Address : ")
    customer = Customer(name,Phone,Email,Address)

    while True:
        print(f"Welcome {customer.name}")
        print("1 : View Menu ")
        print("2 : Add Item to Car ")
        print("3 : View Cart ")
        print("4 : PayBill ")
        print("5 : Exit ")

        ch = int(input("Enter Your Choice : "))
        if ch==1:
            customer.view_menu(mamar_res)
        elif ch==2:
            item_name = input("Enter Item Name : ")
            item_quantity = int(input("Enter Quantity : "))
            customer.add_to_cart(mamar_res,item_name,item_quantity)
        elif ch==3:
            customer.view_cart()
        elif ch==4:
            customer.pay_bil()
        elif ch==5:
            break
        else :
            print("Invalid Input")


def admin_menu():
    name = input("Enter Your Name : ")
    Phone = int(input("Enter Your Phone : "))
    Email = input("Enter Your Email : ")
    Address = input("Enter Your Address : ")
    admin = Admin(name,Phone,Email,Address)

    while True:
        print(f"Welcome {admin.name}")
        print("1 : Add New Item ")
        print("2 : Add New Employee ")
        print("3 : View Employee ")
        print("4 : View Menu ")
        print("5 : Delete Menu ")
        print("6 : Exit ")

        ch = int(input("Enter Your Choice : "))
        if ch==1:
            item_name = input("Enter Item Name : ")
            item_price = int(input("Enter Item Price : "))
            item_quantity = int(input("Enter Item Quantity : "))
            item = FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_res,item)
        elif ch==2:
            Name = input("Enter Employee Name : ")
            Phone = input("Enter Employee Phone : ")
            Email = input("Enter Employee Email : ")
            Address = input("Enter Employee Address : ")
            Age = input("Enter Employee Age : ")
            Designation = input("Enter Employee Designation : ")
            Salary = input("Enter Employee Salary : ")
            admin.add_employee(Name, Phone, Email, Address, Age, Designation, Salary)
        elif ch==3:
            admin.view_employee(mamar_res)
        elif ch==4:
            admin.view_menu(mamar_res)
        elif ch==5:
            item_name = input("Enter Item Name : ")
            admin.delete_item(mamar_res,item_name)
        elif ch==6:
            break
        else :
            print("Invalid Input")


while True:
    print("*****Welcome*****")
    print("1 : Customer ")
    print("2 : Admin ")
    print("3 : Exit ")

    ch = int(input("Enter Your choice : "))
    if ch==1:
        customer_menu()
    elif ch==2:
        admin_menu()
    elif ch==3:
        break
    else :
        print("Invalid Choice")