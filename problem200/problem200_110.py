import sys

A, B, M = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

t = sys.maxsize
for _ in range(M):
    x, y, c = [int(i) for i in input().split()]
    t = min(t, a[x - 1] + b[y - 1] - c)

print(min(t, sorted(a)[0] + sorted(b)[0]))