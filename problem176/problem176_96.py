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
def my_pow(base, n, mod):
    if n == 0:
        return 1
    x = base
    y = 1
    while n > 1:
        if n % 2 == 0:
            x *= x
            n //= 2
        else:
            y *= x
            n -= 1
        x %= mod
        y %= mod
    return x * y % mod

N, K = map(int, input().split())

cnt = [0] * (K + 1)

ans = 0
total = 0
for i in range(K, 0, -1):
    t = K // i
    now = my_pow(t, N, MOD)
    for j in range(i*2, K + 1, i):
        now -= cnt[j]
    cnt[i] = now
    ans += (now * i) % MOD
print(ans % MOD)
