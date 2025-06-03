import sys

n = int(sys.stdin.readline())
for _ in range(n):
    a, b, c = sorted(list(map(int, sys.stdin.readline().split())))
    print('YES' if a * a + b * b == c * c else 'NO')