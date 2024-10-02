s = input()
cnt=0
cnt1=0
str = ""
ans = []
for i in s:
    if i=='L':
        cnt+=1
        str+=i
    elif i=='R':
        cnt-=1
        str+=i
    
    if cnt==0:
        cnt1+=1
        ans.append(str)
        str=""
print(len(ans))
for tmp in ans:
    print(tmp)