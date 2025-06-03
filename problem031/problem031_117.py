from math import *
while True:
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split()))
    sum_s = sum(s)
    m = sum_s / n
    print(sqrt(sum((a - m) ** 2 for a in s) / n))

