exp = input()

if eval(exp.replace("=", "==")):
    print("Yes")

else: 
    print(eval(exp.split("=")[0]))