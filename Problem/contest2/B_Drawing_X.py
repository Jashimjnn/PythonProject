n = int(input())

for i in range(n):
    row = ''
    for j in range(n):
        if i==j and i==n//2:
            row+='X'
        elif i==j:
            row+='\\'
        elif i+j==n-1:
            row+='/'
        else:
            row+='*'
    print(row)