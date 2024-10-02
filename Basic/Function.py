#Function
"""def sum(a,b):
    return a+b
result = sum(4,5)
print(result)
"""


#default perameter
"""def sum(a,b,c=0):
    return a+b+c
result = sum(5,4)
result1 = sum(5,4,3)
print(result)
print(result1)
"""


#many perameter
"""def sum(*args):
    sum=0
    for num in args:
        sum = sum+num
    return sum
result = sum(5,4,3,2,1)
print(result)
"""


#key value perameter
"""def func(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} : {value}')
result = func(apple = 5,orange = 4)
"""


#Global variable
"""balance = 500
def func():
    print(balance)

func() 
print(balance)

def chk():
    global balance
    balance = balance - 5
    print(balance)
chk()
"""