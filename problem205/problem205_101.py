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

N, P = map(int, input().split())
S = input()

if P == 2 or P == 5:
    ans = 0
    for i, c in enumerate(S[::-1]):
        if int(c) % P == 0:
            ans += N - i
    print(ans)
    exit()

cnt = [0] * P
base = 1
cur = 0
for c in S[::-1]:
    cur += (base * int(c)) % P
    cnt[cur % P] += 1
    base *= 10 
    base %= P
ans = 0
for i in cnt:
    if i == 0:
        continue
    ans += i * (i - 1) // 2
print(ans + cnt[0])



