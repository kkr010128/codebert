K = int(input())
S = input().rstrip()
L = len(S)
if L <= K:
    print(S)
else:
    print(S[:K] + "...")