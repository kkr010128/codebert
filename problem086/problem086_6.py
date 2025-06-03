from math import ceil
N, X, T = [int(s) for s in input().split()]
print(ceil(N/X) * T)