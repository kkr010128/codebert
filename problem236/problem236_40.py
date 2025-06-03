import numpy as np

H = int(input())
W = int(input())
N = int(input())

print(int(np.ceil(N/max(H,W))))