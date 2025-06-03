import math
import sys

stdin = sys.stdin

ns = lambda: stdin.readline().rstrip()
ni = lambda: int(stdin.readline().rstrip())
nm = lambda: map(int, stdin.readline().split())
nl = lambda: list(map(int, stdin.readline().split()))
mod = 10**9 + 7 
sys.setrecursionlimit(1000010)


N,M = nm()
used = [0] * N

start = 0
if N % 2 != 0:
    s = (N-1)//2
else:
    s = N//2 - 1 

for i in range(1,M+1):
    q= (i+1)//2
    if i % 2 !=0:
        print(q,N+1-q)
    else:
        print(s+1-q,s+1+q)
