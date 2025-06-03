import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353

S = sys.stdin.buffer.readline().decode().rstrip()
N = len(S)

# ピッタリ払う
dp0 = [INF] * (N + 1)
# 1 多く払う
dp1 = [INF] * (N + 1)

dp0[0] = 0
dp1[0] = 1
for i, c in enumerate(S):
    dp0[i + 1] = min(dp0[i] + int(c), dp1[i] + 10 - int(c))
    dp1[i + 1] = min(dp0[i] + int(c) + 1, dp1[i] + 10 - int(c) - 1)
# print(dp0)
# print(dp1)
print(dp0[-1])
