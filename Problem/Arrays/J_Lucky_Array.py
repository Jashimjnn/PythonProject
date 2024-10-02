n = int(input())
lst = list(map(int,input().split()))
mn = min(lst)
cnt=0
for i in range(0,n,1) :
    if lst[i]==mn:
        cnt+=1
if  cnt%2!=0:
    print("Lucky")
else:
    print("Unlucky")