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
class Library:
    def __init__(self,owner,name):
        self.owner = owner
        self.name = name
        self.books = []
        self.users = []
    def addBook(self,id,name,cat,q):
        book = Book(id,name,cat,q)
        self.books.append(book)
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
            