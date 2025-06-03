
from collections import defaultdict

S = input()
n = len(S)

mod = 2019
d = defaultdict(int)
d[0] = 1
num = 0
for i in reversed(range(n)):
    num += int(S[i]) * pow(10, n - i - 1, mod)
    num %= mod
    d[num] += 1

ans = 0
for v in d.values():
    ans += v * (v - 1) // 2
print(ans)
