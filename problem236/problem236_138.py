import math

H = int(input())
W = int(input())
N = int(input())

for i in range(1, max(H, W)+1):
    if(max(H, W)*i >= N):
        print(i)
        break