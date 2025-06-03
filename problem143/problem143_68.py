K = int(input())
S = input()

if len(S) > K:
    S_short = S[:K]
    print("{}...".format(S_short))
else:
    print(S)