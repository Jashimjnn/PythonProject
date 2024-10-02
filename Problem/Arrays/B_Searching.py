n = int(input())
lst = list(map(int,input().split()))
x = int(input())
idx = 0
flag = False
for i in range(0,n,1):
    if x==lst[i]:
        idx = i
        flag = True
        break
if flag==True:
    print(idx)
else:
    print(-1)