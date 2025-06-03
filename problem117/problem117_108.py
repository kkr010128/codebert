#!/usr/bin/env python
# -*- coding: utf-8 -*-

N, M, K = map(int, input().split())
result = 0 # max
a_time = list(map(int, input().split()))
b_time = list(map(int, input().split()))

sum = 0

a_num = 0
for i in range(N):
    sum += a_time[i]
    a_num += 1
    if sum > K:
        sum -= a_time[i]
        a_num -= 1
        break
i = a_num
j = 0
while i >= 0:
    while sum < K and j < M:
        sum += b_time[j]
        j += 1
    if sum > K:
        j -= 1
        sum -= b_time[j]
    if result < i + j:
        result = i + j
    i -= 1
    sum -= a_time[i]

print(result)
