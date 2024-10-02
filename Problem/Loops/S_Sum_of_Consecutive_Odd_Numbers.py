n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    sum=0
    if a>b:
        for i in range(b+1,a):
            if i%2!=0:
                sum+=i
        print(sum)
    else:
        for i in range(a+1,b):
            if i%2!=0:
                sum+=i
        print(sum)