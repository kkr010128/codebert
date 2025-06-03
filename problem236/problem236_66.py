from math import ceil

H,W,N = map(int, open(0).read().split())
m = max(H,W)
print(ceil(N/m))