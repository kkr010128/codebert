import itertools
import numpy as np

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
nums=np.array(tuple(itertools.permutations(range(1, N+1), N))).tolist()

print(abs(nums.index(P) - abs(nums.index(Q))))