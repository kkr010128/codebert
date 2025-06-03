# author:  Taichicchi
# created: 19.09.2020 00:14:21

import sys

N = int(input())

S = input()

ans = S.count("R") * S.count("G") * S.count("B")


for i in range(N - 2):
    for j in range(i + 1, N - 1):
        try:
            k = 2 * j - i
            if (S[i] != S[j]) & (S[j] != S[k]) & (S[k] != S[i]):
                ans -= 1
        except:
            continue

print(ans)
