import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
H = [int(x) for x in sys.stdin.readline().rstrip().split()]

H.sort()
# print(H[:-K])
if K == 0:
    print(sum(H))
else:
    print(sum(H[:-K]))