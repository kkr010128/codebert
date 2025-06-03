#!/usr/bin/env python3

numbers = input().split(" ")
n = int(numbers[0])
m = int(numbers[1])

numbers = input().split(" ")
h = [int(x) for x in numbers]
h.insert(0, 0)

is_good = [1] * (n + 1)

for i in range(m):
  numbers = input().split(" ")
  a = int(numbers[0])
  b = int(numbers[1])
  if h[a] <= h[b]:
    is_good[a] = 0
  if h[a] >= h[b]:
    is_good[b] = 0

print(is_good.count(1) - 1)
