S = input()

if len(S) % 2 == 0 and S == "hi" * (len(S) // 2 ):
    print("Yes")
else:
    print("No")