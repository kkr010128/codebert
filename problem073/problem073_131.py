import math
import collections
import fractions
import itertools
import functools
import operator
import bisect

N = int(input())

def solve():
    cnt = 0
    for i in range(1, N):
        cnt += (N-1)//i
    print(cnt)
    return 0

if __name__ == "__main__":
    solve()
