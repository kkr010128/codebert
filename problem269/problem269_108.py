import sys
import math
t1, t2 = [int(i) for i in sys.stdin.readline().split()]
a1, a2 = [int(i) for i in sys.stdin.readline().split()]
b1, b2 = [int(i) for i in sys.stdin.readline().split()]
a1 -= b1
a2 -= b2
_sum = a1 * t1 + a2 * t2
if _sum == 0:
    print("infinity")
elif _sum * a1 > 0:
    print("0")
else:
    cnt = (-a1 * t1) / _sum
    res = math.ceil(cnt) * 2 - 1 + (cnt % 1 == 0)
    print(res)