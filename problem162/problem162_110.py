import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

n,m = na()

a,b = 1,n-(n%2)
for i in range(m):
    if n%2 == 0 and i == (m+1)//2:
        a += 1
    print(a,b)
    a,b = a+1, b-1