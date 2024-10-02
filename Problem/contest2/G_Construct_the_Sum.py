n = int(input())

for _ in range(n):
    a,b = map(int,input().split())
    x = a*(a+1)//2
    if x<b:
        print(-1)
        continue
    lst = []
    for i in range(a,1,-1):
        if b>=i and b>0:
            lst.append(i)
            b-=i
    if b==0:
        print(" ".join(map(str,lst)))
    else:
        print(-1)