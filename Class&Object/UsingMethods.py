class Phone:
    price = 20000
    brand = 'Samsung'
    color = 'blue'

    def call(self):
        print('I love Bangladesh')
    
    def send_mass(self,phone,mass):
        txt = f'I send a massege to {phone} and the massege is {mass}'
        return txt
    
my_phone = Phone()
my_phone.call()
result = my_phone.send_mass(1992,'I love you')
print(result)