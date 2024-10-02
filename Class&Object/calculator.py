class calculator:
    
    def add(self,num1,num2):
        return num1+num2
    def sub(self,num1,num2):
        return num1-num2
    def mult(self,num1,num2):
        return num1*num2
    def divide(self,num1,num2):
        return num1//num2

cal = calculator()
x = cal.add(10,20)
print(x)
y = cal.sub(20,10)
print(y)
z = cal.mult(10,20)
print(z)
p = cal.divide(20,10)
print(p)