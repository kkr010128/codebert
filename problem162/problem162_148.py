from collections import Counter
import sys

sys.setrecursionlimit(10 ** 6)

mod = 1000000007
inf = int(1e18)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def inverse(a):
    return pow(a, mod - 2, mod)


def usearch(x, a):
    lft = 0
    rgt = len(a) + 1
    while rgt - lft > 1:
        mid = (rgt + lft) // 2
        if a[mid] <= x:
            lft = mid
        else:
            rgt = mid
    return lft


def main():
    n, m = map(int, input().split())
    ans = []
    for i in range(1, (m+1)//2+1):
        if len(ans) == m:
            break
        ans.append([i, m+2-i])

    for i in range(1, (m+1)//2+1):
        if len(ans) == m:
            break
        ans.append([m+1+i, 2*m+2-i])

    for x in ans:
        print(x[0], x[1])

main()
