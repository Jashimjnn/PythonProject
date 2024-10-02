n = int(input())
sp = n-1
k = 1
for i in range(0,n,1):
    print(" "*sp+"*"*k)
    sp-=1
    k+=2