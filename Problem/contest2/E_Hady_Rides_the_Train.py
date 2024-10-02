n = int(input())
r = n//4
c =0 
if r%2==0:
    c = n%4
else:
    c = 3-(n%4)
print(r,c)