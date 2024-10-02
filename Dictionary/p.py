n = int(input())
lst = []
for i in range(1,n+1,1):
    for x in range(1,i+1,1):
        lst.append('#')
    print("".join(map(str,lst)))
    lst.clear()