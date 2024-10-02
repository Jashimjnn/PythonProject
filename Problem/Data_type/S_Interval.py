x = float(input())
if x>=0 and x<=25.0000:
    print("Interval [0,25]")
elif x>25.00001 and x<=50.0000000:
    print("Interval (25,50]")
elif x>50.00000001 and x<=75.0000000:
    print("Interval (50,75]")
elif x>75.00000001 and x<=100.0000000:
    print("Interval (75,100]")
else:
    print("Out of Intervals")