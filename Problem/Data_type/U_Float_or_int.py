s = input()
a,b = map(int,s.split('.'))
if b>0:
    print("float",a,f"0.{b}")
else:
    print("int",a)