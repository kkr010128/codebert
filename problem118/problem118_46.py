import collections, heapq, itertools, math, functools
groupby = itertools.groupby
rs  = lambda: input()
ri  = lambda: int(input())
rm  = lambda: map(int, input().split())
rai = lambda: [int(x) for x in input().split()]

def solve():
    N = ri()
    ans = 0
    for i in range(1, N + 1):
        n = N // i
        ans += i * n * (n + 1) // 2
    return ans
print(solve())