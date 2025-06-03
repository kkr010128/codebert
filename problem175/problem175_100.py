
from collections import Counter

N = int(input())
S = input()

ctr = Counter(S)
res = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        k = 2 * j - i
        if k < N and (S[i] != S[j] and S[i] != S[k] and S[j] != S[k]):
            res += 1

print(ctr["R"] * ctr["G"] * ctr["B"] - res)
