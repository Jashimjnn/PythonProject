a,b,c = map(int,input().split())

x = (a*b)/c
if x.is_integer():
    if -2147483648 <= x <= 2147483647:
     print("int")
    else:
     print("long long")
else:
  print("double")