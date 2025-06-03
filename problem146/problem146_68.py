MOD = 10 ** 9 + 7
from math import gcd
from collections import defaultdict

n = int(input())
plus = defaultdict(int)
minus = defaultdict(int)
zero = [0, 0, 0]
for _ in range(n):
    a, b = map(int, input().split())
    if a * b == 0:
        if a == b == 0:
            zero[0] += 1
        elif a == 0:
            zero[1] += 1
        else:
            zero[2] += 1
        continue
    g = gcd(a, b)
    a //= g
    b //= g
    if a < 0:
        a *= -1
        b *= -1
    if b >= 0:
        s = str(a) + "-" + str(b)
        plus[s] += 1
    else:
        s = str(-b) + "-" + str(a)
        minus[s] += 1

pm = [[zero[1], zero[2]]]
cnt = sum(zero)
for key, value in plus.items():
    if minus[key] != 0:
        pm.append([value, minus[key]])
        cnt += value + minus[key]
        
ans = pow(2, n - cnt, MOD)

for p, m in pm:
    ans *= (pow(2, p, MOD) + pow(2, m, MOD) - 1)
    ans %= MOD
ans += zero[0] - 1
ans %= MOD
print(ans)
