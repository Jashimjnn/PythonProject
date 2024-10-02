n = int(input())
j = 1
cnt=0
for i in range(n):
    lst = []
    for k in range(0,3,1):
        lst.append(j)
        j+=1
    print(" ".join(map(str,lst)),"PUM")
    j+=1