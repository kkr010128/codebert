N = int(input())
S = input()

if len(S) % 2 != 0:
    print("No")
    exit()

else:
    l = len(S)
    if S[0:l//2] == S[l//2:l]:
        print("Yes")
    else:
        print("No")
