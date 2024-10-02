while True:
    a,b = map(int,input().split())
    if a<=0 or b<=0:
        break
    if a>b:
        sum=0
        lst = []
        for i in range(b,a+1):
            sum+=i
            lst.append(i)
        print(" ".join(map(str,lst)),f"sum ={sum}")
    elif b>a:
        sum=0
        lst = []
        for i in range(a,b+1):
            sum+=i
            lst.append(i)
        print(" ".join(map(str,lst)),f"sum ={sum}")
    else:
        print(a,f"sum ={a}")