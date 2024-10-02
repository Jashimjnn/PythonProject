from math import*
a,b,c = map(int,input().split())
lst = [a,b,c]
mn = min(lst)

p = a-mn
q = b-mn
r = c-mn
if p==0 or r==0:
    print(mn)
else:
    x = p//2
    if x==r:
        y = x+mn
        print(y)
    elif x>r:
        y = r+mn
        print(y)
    else:
        y = x+mn
        print(y)