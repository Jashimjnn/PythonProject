from math import*
a,b,c,d = map(int,input().split())

e = b*log(a)
f = d*log(c)
if e>f:
    print("YES")
else:
    print("NO")