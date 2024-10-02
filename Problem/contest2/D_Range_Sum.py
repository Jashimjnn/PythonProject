n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    ma = max(a,b)
    mi  = min(a,b)
    mi-=1
    sum1=mi*(mi+1)//2
    sum2 = ma*(ma+1)//2
    sum=sum2-sum1
    print(sum)