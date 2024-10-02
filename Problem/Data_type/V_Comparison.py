s = input()
a,ch,b = s.split()
#a,ch,b = map(int,s.split())

if ch=='=':
    ch="==";

if eval(a+ch+b):
    print("Right")
else:
    print("Wrong")