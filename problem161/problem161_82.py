import sys
input = lambda: sys.stdin.readline().rstrip()

A,B,N = map(int, input().split())

def f(x):
    return int(A*x/B) - A*int(x/B)

if N >= B-1:
    print(f(B-1))
else:
    print(f(N)) 