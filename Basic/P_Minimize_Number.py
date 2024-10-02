n = int(input())
lst = list(map(int,input().split()))

cnt=0
while all(i%2==0 for i in lst):
    cnt+=1
    lst = [j//2 for j in lst]
print(cnt)