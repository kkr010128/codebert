import math
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import product
from collections import defaultdict
from collections import deque
from collections import Counter
import heapq


def input_li():
    return list(map(int, input().split()))


N = int(input())
A_LI = input_li()
max_h = A_LI[0]
ans = 0
for i in range(1, N):
    if A_LI[i] < max_h:
        ans += max_h - A_LI[i]
    else:
        max_h = max(max_h, A_LI[i])
print(ans)
