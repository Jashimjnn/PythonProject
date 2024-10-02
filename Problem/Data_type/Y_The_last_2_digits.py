a,b,c,d = map(int,input().split())

a = a%100
b = b%100
c = c%100
d = d%100

e = a*b*c*d
if e%100<=9:
    print(f"0{e%100}")
else:
    print(e%100)