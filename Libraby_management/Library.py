class Book:
    def __init__(self,id,name,cat,quantity):
        self.id = id
        self.name = name
        self.cat = cat
        self.quantity = quantity
class User:
    def __init__(self,id,name,password):
        self.id = id
        self.name = name
        self.password = password
        self.borrowBook = []
        self.returnBook = []
class Library:
    def __init__(self,owner,name):
        self.owner = owner
        self.name = name
        self.books = []
        self.users = []
    def addBook(self,id,name,cat,q):
        book = Book(id,name,cat,q)
        self.books.append(book)
        print(f'{name} Book added !')
    def addUsers(self,id,name,password):
        users = User(id,name,password)
        self.users.append(users)
        return users
    def borrow(self,user,id):
        for book in self.books:
            if book.id == id:
                if book in user.borrowBook:
                    print('Already Borrowed!')
                    return
                elif book.quantity<1:
                    print('Not available')
                    return
                else:
                    user.borrowBook.append(book)
                    book.quantity-=1
                    print(f'{book.name} borrowed successfully !')
        print('Book not found')
    
p1 = Library('Khurshida apu','Phitron Library')
admin = p1.addUsers(1,'admin','admin')
Rahim = p1.addUsers(50,'Rahim','1234')

pybokk = p1.addBook(15,'Dune','Sci-fic',5)

run = True
currentUser = admin
while run:
    if currentUser==None:
        print('No User logged')
        option = input('Loging ? Register (L/R) : ')
        if option=='R':
            id = int(input('Enter id : '))
            name = input('Enter name : ')
            password = input('Enter password : ')
            user = p1.addUsers(id,name,password)
            currentUser = user
        elif option =='L':
            id = int(input('Enter : '))
            password = input('Enter password : ')
            match = False
            for user in p1.users:
                if user.id == id and user.password==password:
                    currentUser = user
                    match = True
                    break
            if match==False:
                print('No user found')
    else :
        if currentUser.name=='admin':
            print('Option : ')
            print('1 : Add Book : ')
            print('2 : Show User : ')
            print('3 : Show Bool : ')
            print('4 : Logout : ')

            ch = int(input('Enter option : '))
            if ch==1:
                id = int(input('Enter id : '))
                name = input('Enter name : ')
                cat = input('Enter cat : ')
                q = int(input('Enter Quantity : '))
                p1.addBook(id,name,cat,q)
            elif ch == 2:
                for user in p1.users:
                    print(f'User ID: {user.id}, Name: {user.name}')
            elif ch == 3:
                for book in p1.books:
                    print(f'Book ID: {book.id}, Name: {book.name}, Category: {book.cat}, Quantity: {book.quantity}')
            elif ch == 4:
                currentUser = None
        else:
            print('Option :')
            print('1:Borrow Book : ')
            print('2 : Return Book : ')
            print('3 : Show Book : ')
            print('4 : Show borrowed book : ')
            print('5 : Show returned book : ')
            print('6 : Logout : ')
            ch = int(input('Enter option : '))
            if ch==1:
                id = int(input('Enter id : '))
                p1.borrow(currentUser,id)
