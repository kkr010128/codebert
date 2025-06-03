#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))
ans = 1000
left = 0
right = 0
while left < n:
    right = left
    while right + 1 < n and a[right] <= a[right + 1]:
        right += 1
    ans = ans // a[left] * a[right] + ans % a[left]
    left = right
    left += 1
print(ans)
