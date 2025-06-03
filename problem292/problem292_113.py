from itertools import combinations
import numpy as np
N = int(input())
D = list(map(int, input().split()))
List = np.array(list(combinations(D,2)))
print(sum(np.product(List, axis = 1)))


