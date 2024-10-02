n = int(input())
y = n//365
n = n%365
m = n//30
n = n%30
print(y,"years")
print(m,"months")
print(n,"days")