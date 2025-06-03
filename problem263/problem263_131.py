import sys
input = sys.stdin.readline
from collections import defaultdict, deque

n, s, res, MOD = int(input()), list(map(int, input().split())), 0, int(1e9) + 7
for i in range(61):
    x, c = int(pow(2, i, MOD)), [0, 0]
    for j in range(n): c[1 if s[j] & 1 << i else 0] += 1
    x = (x * c[0]) % MOD; x = (x * c[1]) % MOD; res = (res + x) % MOD
print(res)