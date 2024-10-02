n = int(input())
numbers = list(map(int, input().split()))

cnte=0
cnto=0
cntp=0
cntn=0
for x in numbers:
    if x%2==0:
        cnte+=1
    if x>0:
        cntp+=1
    if x<0:
        cntn+=1
    if x%2!=0:
        cnto+=1

print(f"Even: {cnte}")
print(f"Odd: {cnto}")
print(f"Positive: {cntp}")
print(f"Negative: {cntn}")