import math

n = int(input())

# nが奇数ならば必ず0
if n % 2 == 1:
    print(0)
else:
    s = 0
    p = 0
    while 10 * (5 ** p) <= n:
        s += n // (10 * (5 ** p))
        p += 1
    print(s)
