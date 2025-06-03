from sys import stdin
a, b = map(int, stdin.readline().rstrip().split())

ans = max(0, a - 2 * b)
print(ans)
