import sys
input = sys.stdin.readline
mod = 10**9 + 7
n = int(input())
ab = [[int(x) for x in input().split()] for _ in range(n)]
from collections import defaultdict, Counter
import math
double_zero_cnt = 0
a_zero_cnt = 0
b_zero_cnt = 0
d = defaultdict(list) # [a, b] ngのそれぞれの個数
a_b = []
for a, b in ab:
    if a == 0 and b == 0: 
        double_zero_cnt += 1
        continue
    elif a == 0:
        a_zero_cnt += 1
        continue
    elif b == 0:
        b_zero_cnt += 1
        continue
    g = math.gcd(a, b)
    a //= g
    b //= g
    if b < 0:
        b *= (-1)
        a *= (-1) # 必ずbは正
    a_b.append((a, b))
c = Counter(a_b)
key_list = list(c.keys())
for key in key_list:
    a, b = key
    if a < 0:
        a_ = a*(-1)
        b_ = b*(-1)
    else:
        a_ = a
        b_ = b
    if d[(-b_, a_)] != []:
        continue
    if c[(-b_, a_)] != 0:
        d[(a, b)] = [c[(a, b)], c[(-b_, a_)]]
ans = 1
used_cnt = double_zero_cnt
for key in d.keys():
    if d[key] == []:
        continue
    x, y = d[key]
    used_cnt += (x + y)
    mul = (pow(2, x, mod) + pow(2, y, mod) - 1) % mod
    ans *= mul
    ans %= mod
if a_zero_cnt > 0 and b_zero_cnt > 0:
    ans *= (pow(2, a_zero_cnt, mod) + pow(2, b_zero_cnt, mod) - 1)
    ans %= mod
    used_cnt += a_zero_cnt + b_zero_cnt
elif a_zero_cnt > 0:
    ans *= pow(2, a_zero_cnt, mod)
    ans %= mod
    used_cnt += a_zero_cnt
elif b_zero_cnt > 0:
    ans *= pow(2, b_zero_cnt, mod)
    ans %= mod
    used_cnt += b_zero_cnt
ans *= pow(2, n - (used_cnt), mod)
ans %= mod
ans -= 1
ans += double_zero_cnt
ans %= mod
print(ans)





