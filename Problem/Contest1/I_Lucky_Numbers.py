a = int(input())
b = a//10
c = a%10
if c==0 or (b%c==0 or c%b==0):
    print("YES")
else:
    print("NO")