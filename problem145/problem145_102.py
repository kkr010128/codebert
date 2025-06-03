#create date: 2020-07-02 22:54

import sys
stdin = sys.stdin
from collections import deque

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n, m = na()
    g = [[] for i in range(n)]
    for i in range(m):
        a, b = na()
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    q = deque([0])
    d = [-1] * n
    d[0] = 0
    while q:
        v = q.popleft()
        for w in g[v]:
            if d[w] != -1:
                continue
            d[w] = v
            q.append(w)
    if -1 in d:
        print("No")
    else:
        print("Yes")
        for di in d[1:]:
            print(di+1)


if __name__ == "__main__":
    main()