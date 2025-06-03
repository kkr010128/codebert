#!/usr/bin/env python3
import sys
from collections import Counter
input = sys.stdin.readline
INF = 10**9

n, k = [int(item) for item in input().split()]
a = [int(item) - 1 for item in input().split()]
cumsum = [0] * (n + 1)
for i in range(n):
    cumsum[i+1] = cumsum[i] + a[i]
    cumsum[i+1] %= k

ls = list(set(cumsum))
dic = dict()
for i, item in enumerate(ls):
    dic[item] = i

cnt = [0] * (n + 10)
num = 0
ans = 0
for i, item in enumerate(cumsum):
    index = dic[item]
    ans += cnt[index]
    cnt[index] += 1
    num += 1
    if num >= k:
        left = cumsum[i - k + 1]
        index = dic[left]
        if cnt[index] > 0:
            cnt[index] -= 1
        num -= 1

print(ans)