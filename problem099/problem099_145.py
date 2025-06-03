from sys import stdin

input = stdin.readline
import math
import heapq


def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    left = 1
    right = max(a)

    def ok(l):
        s = sum([(i-1) // l for i in a])
        return s <= k
    while left < right:
        mid = (left + right) // 2
        if ok(mid):
            right = mid
        else:
            left = mid + 1
    print(left)


if __name__ == '__main__':
    solve()
