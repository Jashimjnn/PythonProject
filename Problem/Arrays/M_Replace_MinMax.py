n = int(input())
lst = list(map(int,input().split()))
mn = min(lst)
mx = max(lst)
# print(mx,mn)
for i in range(0,n,1):
    if lst[i]==mn:
        lst[i]=mx
    elif lst[i]==mx:
        lst[i]=mn
print(" ".join(map(str,lst)))