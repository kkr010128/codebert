S = input()
T = input()

if T.startswith(S):
    if len(T)-len(S)==1:
        print("Yes")
    else:
        print("No")
else:
    print("No")