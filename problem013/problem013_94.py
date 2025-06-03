# -*- Coding: utf-8 -*-

nums = int(input())
a = [int(input()) for i in range(nums)]

minv = a[0]
maxv = -2000000000

for i in range(1, nums):
    maxv = max(maxv, a[i] - minv)
    minv = min(minv, a[i])

print(maxv)

