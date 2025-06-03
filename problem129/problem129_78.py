n = int(input())
A = sorted(list(map(int, input().split())))
from collections import Counter
c = Counter(A)

MAX = 10 ** 6 + 1000
dp = [True] * MAX

for k, v in c.items():
    if dp[k] == False: continue
    if v > 1: dp[k] = False
    for x in range(k + k, MAX, k):
        dp[x] = False

res = 0
for x in range(n):
    if dp[A[x]]: res += 1
print(res)