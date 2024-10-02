n = int(input())
for i in range(1,n+1,1):
    x = int(input())
    y = 1
    for j in range(1,x+1,1):
        y*=j
    print(y)