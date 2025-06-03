import sys

n = int(input())
for i in range(n):
    a = sorted(list(map(int, sys.stdin.readline().split())))
    print('YES' if a[0] ** 2 + a[1] ** 2 == a[2] ** 2 else 'NO')