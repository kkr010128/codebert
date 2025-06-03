import math
import collections
import fractions
import itertools
import functools
import operator

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k, n):
        print("Yes") if a[i] > a[i-k] else print("No")
    return 0

if __name__ == "__main__":
    solve()