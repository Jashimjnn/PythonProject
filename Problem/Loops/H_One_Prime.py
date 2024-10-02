n = int(input())
flag = True
for i in range(2,n,1):
    if n%i==0:
        flag = False
if flag==True:
    print("YES")
else:
    print("NO")