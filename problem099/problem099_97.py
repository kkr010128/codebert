import heapq
import math

def solve():
    N, K = map(int, input().split())
    A = sorted(map(int, input().split()), reverse=True)
    l = 0
    r = A[0]
    # (l, r]
    #print(A)
    #print("K=",K)
    while r - l> 1:
        m = (r + l) // 2
        cuts = 0
        for a in A:
            cuts += (a-1) // m
        #print(l, m,r, cuts)
        if cuts <= K:
            r = m
        else:
            l = m
    print(r)

solve()