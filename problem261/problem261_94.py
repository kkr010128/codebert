import sys

S = sys.stdin.readline().strip()
ls = len(S)

ans = 0
h = ls // 2
for i in range(h):
    if S[i] != S[ls - 1 - i]:
        ans += 1

print(ans)