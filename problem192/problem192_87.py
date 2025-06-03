import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
A = LI()

c = collections.Counter(A)


cnt = 0
for _ in c:
    cnt += c[_] * (c[_] - 1) // 2

for i in range(N):
    a = c[A[i]]
    print(cnt - (a - 1))
