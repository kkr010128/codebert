from fractions import gcd
from functools import reduce
import numpy as np

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm(numbers):
    return reduce(lcm_base, numbers, 1)

N, M = map(int, input().split())

A = list(map(int, input().split()))
A = list(map(lambda x: x // 2 , A))
A = np.array(A)

l = lcm(A)

if ((l//A % 2 == 1).sum() != N):
    print(0)
else:
    ans = (M//l + 1) // 2
    print(ans)