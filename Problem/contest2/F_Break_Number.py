n = int(input())
lst = list(map(int,input().split()))
lst1 = []
for i in lst:
    cnt=0
    while i!=0:
        if i%2!=0:
            break
        else:
            cnt+=1
            i//=2
    lst1.append(cnt)
mx = max(lst1)
print(mx)