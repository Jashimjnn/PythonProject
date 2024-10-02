s = input()
ans =0

if '+' in s:
    a,b = map(int,s.split('+'))
    ans += a+b
elif '-' in s:
    a,b = map(int,s.split('-'))
    ans += a-b
elif '*' in s:
    a,b = map(int,s.split('*'))
    ans += a*b;
else:
    a,b = map(int,s.split('/'))
    ans += a//b

print(ans)