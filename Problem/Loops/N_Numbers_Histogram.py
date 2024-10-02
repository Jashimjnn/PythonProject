s = input()
n = int(input())
lst = list(map(int,input().split()))
lst1 = []
for x in lst:
    for i in range(1,x+1,1):
        lst1.append(s)
    print("".join(map(str,lst1)))
    lst1.clear()