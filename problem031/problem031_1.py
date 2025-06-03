import math
n = int(input())
while n:
    s = list(map(float, input().split()))
    m = sum(s) / n
    tmp = 0
    for si in s:
        tmp += (si - m) ** 2
    print(math.sqrt(tmp / n))
    n = int(input())