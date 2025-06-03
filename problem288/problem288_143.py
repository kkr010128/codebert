# 問題: https://atcoder.jp/contests/abc144/tasks/abc144_c

import math

n = int(input())
a = int(math.sqrt(n))
b = 0
while b == 0:
    if n % a > 0:
        a -= 1
        continue
    b = n / a

res = a + b - 2
print(int(res))

