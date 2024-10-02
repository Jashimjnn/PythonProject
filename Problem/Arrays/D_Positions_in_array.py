n = int(input())
A = list(map(int,input().split()))
for i in range(0,n,1):
    if A[i]<=10:
        print(f"A[{i}]","=",A[i])