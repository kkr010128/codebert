import sys
sys.setrecursionlimit(1000000000)
from itertools import count
from collections import defaultdict
ii = lambda: int(input())
mis = lambda: map(int, input().split())
lmis = lambda: list(mis())
INF = float('inf')
def meg(f, ok, ng):
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if f(mid):
            ok=mid
        else:
            ng=mid
    return ok
#


def main():
    N, K = mis()
    A = [0] + lmis()
    for i in range(1, len(A)):
        A[i] = ((A[i] - 1) + A[i-1]) % K
    #
    C = defaultdict(int)
    ans = 0
    for i in range(len(A)):
        if i >= K:
            C[A[i-K]] -= 1
        a = A[i]
        ans += C[a]
        C[a] += 1
    print(ans)

main()
