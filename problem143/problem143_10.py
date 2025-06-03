K = int(input())
S = input()
if len(S) <= K:
    print(S)
else:
    print("{0}...".format(S[0:K]))