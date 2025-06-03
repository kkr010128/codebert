import sys,math,collections,itertools
input = sys.stdin.readline

A,B,N = list(map(int,input().split()))

if B <= N:
    x =B-1
else:
    x = N
print(math.floor(A*x/B) - A * math.floor(x/B))
