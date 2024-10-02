# t = int(input())

# for _ in range(t):
#     n = int(input())
#     lst = list(map(int, input().split()))
#     lst2 = []
    
#     for i in range(n):
#         mx = lst[i]
#         for j in range(i, n):
#             mx = max(mx, lst[j])
#             lst2.append(mx)
    
#     print(" ".join(map(str, lst2)))


t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst2 = []
    
    for i in range(n):
        subarray = []
        for j in range(i, n):
            subarray.append(lst[j])
            lst2.append(subarray[:])  
    
    for subarray in lst2:
        print(subarray)
