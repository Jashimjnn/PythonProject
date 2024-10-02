from math import *
s = input()
ss = s.split()
a = int(ss[0])
b = int(ss[1])
c = int(ss[2])

mx = a
if(mx<b):
    mx = b
if mx<c:
    mx = c

mn = a
if mn>b:
    mn = b
if mn>c:
    mn = c

print(mn,mx)