#Normal

# numbers = [45, 87, 96, 65, 43, 90, 85, 14, 26, 61, 70]
# num = []
# for x in numbers:
#     num.append(x+2)
# print(num)

#In list
# numbers = [45,87,96,65,43,90,85,14,26,61,70]
# num = [x+2 for x in numbers]
# print(num)

#If in list
# numbers = [45,87,96,65,43,90,85,14,26,61,70]
# num = [x for x in numbers if x%2==0 if x%5==0]
# print(num)

#nested loop
players = ['sakib', 'musfik', 'liton']
ages = [38, 37, 32]
num = [[x,y] for x in players for y in ages]
print(num)