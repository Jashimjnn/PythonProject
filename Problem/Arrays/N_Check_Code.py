a,b = map(int,input().split())
str = input()
if str[a]=='-' and str[a+1:].isdigit() and str[:a].isdigit():
    print("Yes")
else:
    print("No")