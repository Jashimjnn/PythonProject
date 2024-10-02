a,b,c,d = map(int,input().split())


if (c>b and d>b) or (c<a and d<a):
    print(-1)
else:
    print(max(a,c),min(b,d))