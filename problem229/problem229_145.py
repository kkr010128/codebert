# -*- coding: utf-8 -*-
H, N = map(int, input().split(' '))
nums = [float('inf') for _ in range(H+1)]
nums[0] = 0

for _ in range(N):
    a, b = map(int, input().split(' '))
    for i in range(H + 1):
        j = min(H, i+a)
        nums[j] = min(nums[j], nums[i] + b)

print(nums[H])