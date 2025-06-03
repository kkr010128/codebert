S = input()
if S.count("R") == 3:
    print(3)
elif S.count("R") == 2:
    if S[1] == "S":
        print("1")
    else:
        print("2")
elif S.count("R") == 1:
    print("1")
else:
    print("0")