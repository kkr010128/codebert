import math

H = int(input())
W = int(input())
N = int(input())

Max = max(H,W)

print(math.ceil(N/Max))