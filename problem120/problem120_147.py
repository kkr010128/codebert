import sys

N, K = map(int, sys.stdin.readline().split())
P = list(map(int, sys.stdin.readline().split()))

P.sort()
print(sum(P[0:K]))