import sys
import math
input = lambda: sys.stdin.readline().rstrip()

N,X, T = map(int, input().split())
print(math.ceil(N/X)*T)