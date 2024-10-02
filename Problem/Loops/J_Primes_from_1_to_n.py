n= int(input())
lst=[]
for i in range(2,n+1):
    flag = True
    for j in range(2,i):
        if i%j==0:
            flag=False
            break

    if flag==True:
        lst.append(i)
print(" ".join(map(str, lst)))