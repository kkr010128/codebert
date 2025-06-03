from __future__ import division, print_function
from sys import stdin
n = int(stdin.readline())
result = [0, 0]
for _ in range(n):
    taro, hanako = stdin.readline().split()
    if taro > hanako:
        result[0] += 3
    elif taro < hanako:
        result[1] += 3
    else:
        result[0] += 1
        result[1] += 1
print(*result)