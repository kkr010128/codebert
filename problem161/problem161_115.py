import sys
def input(): return sys.stdin.readline().rstrip()

A, B, N = map(int, input().split())

if B <= N:
    N = B - 1

print((A*N)//B - A*(N//B))