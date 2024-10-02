a,b = map(int,input().split())
cnt=0
for i in range(a+1):
    for j in range(a+1):
        if (b-i-j)>=0 and (b-i-j)<=a:
            cnt+=1
print(cnt)