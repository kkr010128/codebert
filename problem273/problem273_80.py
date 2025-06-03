#!/usr/bin/env python3
from itertools import accumulate
n, k = map(int, input().split())
a = list(map(int, input().split()))
s = [0] + list(accumulate(a))


def f(x):
    return (x + n * k) % k


ans = 0
dic = {}
for i in range(n + 1):
    if i >= k:
        prev = f(s[i - k] - (i - k))
        dic[prev] -= 1

    cur = f(s[i] - i)
    if cur in dic:
        ans += dic[cur]
        dic[cur] += 1
    else:
        dic[cur] = 1

print(ans)
