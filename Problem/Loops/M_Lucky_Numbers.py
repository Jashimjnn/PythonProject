a,b = map(int,input().split())
lst = []
flag = 0
for i in range(a,b+1,1):
    x = i
    s = 0
    while x!=0:
        if x%10!=4 and x%10!=7:
            s+=1
        x//=10
    if s==0:
        lst.append(i)
        flag+=1
if flag==0:
    print(-1)
else:
    print(" ".join(map(str,lst)))