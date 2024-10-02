n = int(input())
A = list(map(int,input().split()))
mx = A[0]
idx =0
lst = []
for i in range(n-1,-1,-1):
    lst.append(A[i])
print(" ".join(map(str,lst)))