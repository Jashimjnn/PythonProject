n = int(input())
sum=0
x = n
while x!=0:
    y = x%10
    sum = sum*10+y
    x = x//10
if sum==n:
    print(sum)
    print("YES")
else:
    print(sum)
    print("NO")