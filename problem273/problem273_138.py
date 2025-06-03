# AtCoder Beginner Contest 146
# E - Rem of Sum is Num
# https://atcoder.jp/contests/abc146/tasks/abc146_e
from collections import defaultdict
N, K = map(int, input().split())
*A, = map(int, input().split())

A = [0]+A
d = []
c = defaultdict(int)
x = 0
ans = 0
for i, a in enumerate(A):
    x += a - 1
    x %= K

    d.append(x)
    if i-K >= 0:
        c[d[i-K]] -= 1
    ans += c[x]
    c[x] += 1

print(ans)