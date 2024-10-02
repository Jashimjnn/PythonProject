n,a,b = map(int,input().split())
sum1=0
for i in range(1,n+1,1):
    sum=0
    x = i
    while x!=0:
        y = x%10
        sum+=y
        x//=10
    if sum>=a and sum<=b:
        sum1+=i
print(sum1)