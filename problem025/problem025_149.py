N = int(input().rstrip())
A = [int(_) for _ in input().rstrip().split(" ")]
Q = int(input().rstrip())
M = [int(_) for _ in input().rstrip().split(" ")]

import itertools

from functools import lru_cache

@lru_cache(maxsize=2**12)
def solve(i, m):
    if m == 0:
        return True
    elif i >= N:
        return False
    res = solve(i+1, m) or solve(i+1, m - A[i])
    return res
        
        
for m in M:
    if solve(0, m):
        print("yes")
    else:
        print("no")
