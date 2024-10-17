
from Shop import Restaurant
from user import Customer,Sellers
from Fooditem import FoodItem
mamar_res = Restaurant("Mamar Restaurant")
def customer_menu():
    print("Create Your Account : ")
    Email = input("Enter Your Email : ")
    Password = input("Enter Your Password : ")
    customer = Customer(Email,Password)

    while True:
        print(f"Welcome {customer.email}")
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
    Email = input("Enter Your Email : ")
    Password = input("Enter Your Password : ")
    admin = Sellers(Email,Password)

    while True:
        print(f"Welcome {admin.email}")
        print("1 : Add New Item ")
        print("2 : View Menu ")
        print("3 : Delete Menu ")
        print("4 : Exit ")

        ch = int(input("Enter Your Choice : "))
        if ch==1:
            item_name = input("Enter Item Name : ")
            item_price = int(input("Enter Item Price : "))
            item_quantity = int(input("Enter Item Quantity : "))
            item = FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_res,item)
        elif ch==2:
            admin.view_menu(mamar_res)
        elif ch==3:
            item_name = input("Enter Item Name : ")
            admin.delete_item(mamar_res,item_name)
        elif ch==4:
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
        print('No User logged')
        option = input('Loging ? Register (L/R) : ')
        if option=='R':
            Email = input("Enter Your Email : ")
            Password = input("Enter Your Password : ")
            customer_menu()
        elif option =='L':
            Email = input("Enter Your Email : ")
            Password = input("Enter Your Password : ")
            match = False
            for user in mamar_res.employee:
                if user.email == Email and user.password==Password:
                    currentUser = user
                    match = True
                    break
            if match==True:
                customer_menu()
            else:
                print('No user found')
            
    elif ch==2:
        admin_menu()
    elif ch==3:
        break
    else :
        print("Invalid Choice")