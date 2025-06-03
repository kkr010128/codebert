import math
import collections
import fractions
import itertools
import functools
import operator
import bisect

def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ruia, ruib = [0], [0]
    for i in range(n): ruia.append(a[i]+ruia[i])
    for i in range(m): ruib.append(b[i]+ruib[i])
    ans = 0
    j = m
    for i in range(n+1):
        if ruia[i] > k:
            break
        while(ruib[j]>k-ruia[i]):
            j -= 1
        ans = max(ans, i+j)
    print(ans)
    return 0

if __name__ == "__main__":
    solve()