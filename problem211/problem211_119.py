import sys

stdin = sys.stdin

ni = lambda: int(ns())
ns = lambda: stdin.readline().rstrip()
na = lambda: list(map(int, stdin.readline().split()))

# code here
N, R = na()


if N >= 10:
    print(R)
else:
    print(R + 100*(10-N))
