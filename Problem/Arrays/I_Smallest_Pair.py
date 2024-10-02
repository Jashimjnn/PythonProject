t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))

    lst1 = []
    for i in range(0,n,1):
        for j in range(i+1,n,1):
            x=lst[i]+lst[j]+(j+1)-(i+1)
            lst1.append(x)
    print(min(lst1))