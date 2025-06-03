#create date: 2020-06-30 22:48

import sys
stdin = sys.stdin
from itertools import product

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n = ni()
    t = [[-1] * n for _ in range(n)]
    for j in range(n):
        a = ni()
        for i in range(a):
            x, y = na()
            t[j][x-1] = y
    l = list(product([0, 1], repeat=n))
    ans = 0
    #print(t)
    for li in l:
        f = True
        for i in range(n):
            people = li[i]
            if people:
                for j in range(n):
                    if t[i][j] == 1 and li[j] == 0:
                        f = False
                    if t[i][j] == 0 and li[j] == 1:
                        f = False
        if f:
            #print(li, f)
            ans = max(ans, sum(li))
    print(ans)

if __name__ == "__main__":
    main()