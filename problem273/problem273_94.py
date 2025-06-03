import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

import sys
import itertools
# import numpy as np
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
N, K = map(int, input().split())
A = list(map(int, input().split()))

acc = [0] * (N + 1)
for i in range(1, N + 1):
    acc[i] = acc[i - 1] + A[i - 1] - 1
    acc[i] %= K

mp = defaultdict(int)
ans = 0
for j in range(N + 1):
    if j >= K:
        mp[acc[j - K]] -= 1
    ans += mp[acc[j]]
    mp[acc[j]] += 1
print(ans)