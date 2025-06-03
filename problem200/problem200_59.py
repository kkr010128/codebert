import sys

A, B, M = map(int, input().split())

a = list(map(int, sys.stdin.readline().rsplit()))
b = list(map(int, sys.stdin.readline().rsplit()))

res = min(a) + min(b)

for i in range(M):
    x, y, c = map(int, input().split())
    res = min(res, a[x - 1] + b[y - 1] - c)

print(res)
