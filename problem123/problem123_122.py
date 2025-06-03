import numpy as np
import sys 

readline = sys.stdin.readline 

N = int(input())
A = np.array(readline().split(), np.int64)
all_xor = 0
for a in A:
    all_xor = all_xor^a

for a in A:
    xor = all_xor^a
    print(xor, end = ' ')