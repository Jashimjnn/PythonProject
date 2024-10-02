n = int(input())
for i in range(n):
    cnt=0
    x = int(input())
    while x!=0:
        y = x%2
        if y==1:
            cnt+=1
        x//=2
    sum=0
    for j in range(0,cnt,1):
        sum+=(pow(2,j))
    print(sum)