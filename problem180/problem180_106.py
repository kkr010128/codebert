import math
import collections
import fractions
import itertools
import functools
import operator
import bisect

def solve():
    n, k = map(int, input().split())
    print(min(n%k, k-(n%k)))
    return 0

if __name__ == "__main__":
    solve()