n = int(input())
lst = list(map(int,input().split()))
for i in range(0,n,1):
    if lst[i]<0:
        lst[i] = 2
    elif lst[i]>0:
        lst[i] = 1
print(" ".join(map(str,lst)))