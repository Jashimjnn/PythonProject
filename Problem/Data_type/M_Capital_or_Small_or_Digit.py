s = input()

if s.isdigit():
    print("IS DIGIT")
elif s.isalpha():
    print("ALPHA")
    if s.isupper():
        print("IS CAPITAL")
    else:
        print("IS SMALL")