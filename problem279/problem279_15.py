import sys
N = int(input())
S = list(input())

if len(S)%2 != 0:
    print("No")
    sys.exit(0)
else:
    i = int(len(S)/2)
    T = S[0:i]
    if T*2 == S:
        print("Yes")
    else:
        print("No")