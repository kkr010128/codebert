#create date: 2020-06-30 14:42

import sys
stdin = sys.stdin
from itertools import combinations_with_replacement

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n, m, q = na()
    matrix = list()
    for i in range(q):
        matrix.append(na())
    l = list(combinations_with_replacement(range(1, m+1), n))
    ans = 0
    for li in l:
        res = 0
        for q in matrix:
            a, b, c, d = q
            if li[b-1] - li[a-1] == c:
                res += d
        ans = max(ans, res)
    print(ans)

if __name__ == "__main__":
    main()