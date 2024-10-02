n = int(input())
A = list(map(int,input().split()))
mx = A[0]
idx =0
for i in range(0,n,1):
    if mx>A[i]:
        mx = A[i]
        idx = (i+1)

if mx==A[0]:
    print(mx,1)
else:
    print(mx,idx)