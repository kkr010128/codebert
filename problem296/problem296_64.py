#!/usr/bin/env python3
s = input()
n = len(s)
k = int(input())
if s.count(s[0]) == n:
    print(n * k // 2)
    exit()
# pre,post を数えた上で前から連続しているやつの長さを数えて和をとる
ans = 0  # k倍する前をおく
cnt = 1
pre, post = 0, 0
pre_bit = 1
for i in range(n - 1):
    if s[i] == s[i + 1]:
        cnt += 1
    else:
        ans += cnt // 2
        if pre_bit:
            pre = cnt
            pre_bit = 0
        cnt = 1

ans += cnt // 2
post = cnt
if s[0] != s[-1]:
    print(ans * k)
else:
    print(ans * k + (k - 1) * (-1 * (pre // 2 + post // 2) + (pre + post) // 2))
