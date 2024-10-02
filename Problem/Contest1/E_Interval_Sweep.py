a,b = map(int,input().split())
if abs(a-b)==1 or (a==b and a!=0 and b!=0):
    print("YES")
else:
    print("NO")