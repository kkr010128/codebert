#!/usr/bin/env python3
n = int(input())
R = []
for _ in range(n):
    i = int(input())
    R.append(i)

i = 0
j = 0
m = -float("inf")
while j < n - 1:
    j += 1
    if R[j] - R[i] > m:
        m = R[j] - R[i]
    if R[i] > R[j]:
        i = j
print(m)