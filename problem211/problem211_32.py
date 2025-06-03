import sys

N, R = map(int, sys.stdin.readline().split())
print(R if 10 <= N else R + 100 * (10 - N))