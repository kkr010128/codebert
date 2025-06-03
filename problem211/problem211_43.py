from sys import stdin
input = lambda: stdin.readline().rstrip()
n, r = map(int, input().split())
print(r + 100 * max(0, (10 - n)))
