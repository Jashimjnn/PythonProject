a,b = map(int,input().split())

lst = list(map(int,input().split()))
lst1 = []
lst2 = []
cnt=0
for i in range(a):
    if cnt==b:
        cnt=0
        mn = min(lst1)
        lst1.clear()
        lst2.append(mn)
        lst1.append(lst[i])
        cnt+=1
    else:
        lst1.append(lst[i])
        cnt+=1

if cnt!=0:
    mn = min(lst1)
    lst2.append(mn)
print(" ".join(map(str,lst2)))