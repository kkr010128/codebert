inf = float("inf")

S = input()



N = len(S)
bestP = [None for i in range(N)]
bestD = [None for i in range(N)]
if S[0] in ["?", "D"]:
    bestP[0] = 0
    bestD[0] = 1
else:
    bestP[0] = 0
    bestD[0] = 0
for i in range(1, N):
    bestP[i] = max(bestD[i - 1], bestP[i - 1])
    bestD[i] = max(bestD[i - 1] + 1, bestP[i - 1] + 2)
    if S[i] != "?":
        if S[i] == "P":
            bestD[i] = -inf
        else:
            assert S[i] == "D"
            bestP[i] = -inf

ans = [None for i in range(N)]
if bestP[-1] > bestD[-1]:
    ans[-1] = 'P'
else:
    ans[-1] = 'D'
for i in range(N - 2, -1, -1):
    if S[i] != '?':
        ans[i] = S[i]
    else:
        prev = ans[i + 1]
        if prev == 'D':
            if bestP[i] + 2 > bestD[i] + 1:
                ans[i] = 'P'
            else:
                ans[i] = 'D'
        else:
            if bestP[i] > bestD[i]:
                ans[i] = 'P'
            else:
                ans[i] = 'D'

print(''.join(ans))