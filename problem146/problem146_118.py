#!/usr/bin/env python3
#E

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

"""
[本番中]
全体から引くことを考えていたが, 考えることが多く解けなかった

[解説AC]
Ai=0かつBi=0は他の全てと仲が悪いので, 単体で用いるしかない(最後に足す)

Ai*Aj + Bi*Bj = 0の式から内積が思い浮かぶ
仲が悪いペアはAi*Bi >= 0 と Aj*Bj <= 0の場合しかないことがわかる
X: Ai*Bi > 0の場合の(|Ai|, |Bi|)の数
y: Ai*Bi < 0の場合の(|Bi|, |Ai|)の数とすると, 
xとyで同じ(A, B)のペアがあると仲が悪い可能性がある
この場合, 以下の3通りのみ使用できる
xのみで使用(少なくとも1つ) or yのみで使用(少なくとも1つ) or xもyも使用しない
つまり, 2**x[(A, B)] - 1 + 2**y[(A, B)] -1 + 1 = 2**x[(A, B)] + 2**y[(A, B)] - 1
これらの積をとり, 最後に全て使用しなかった場合の1を引いた値が答え(最後に(A,B)=(0,0)を足す必要がある)
"""

n = I()
ab = [LI() for _ in range(n)]

x = defaultdict(lambda : 0)
y = defaultdict(lambda : 0)
z = defaultdict(lambda : 0)
tmp = 0
for a, b in ab:
    if a == 0 and b == 0:
        tmp += 1
    elif a == 0:
        x[0] += 1
        z[0] = 1
    elif b == 0:
        y[0] += 1
        z[0] = 1
    else:
        if a * b > 0:
            g = math.gcd(a, b)
            a //= g
            b //= g
            x[(abs(a), abs(b))] += 1
            z[(abs(a), abs(b))] = 1
        else:
            g = math.gcd(a, b)
            a //= g
            b //= g
            y[(abs(b), abs(a))] += 1
            z[(abs(b), abs(a))] = 1

ans = 1
for i in z.keys():
    ans *= (2**x[i] + 2**y[i] - 1)
    ans %= mod
ans -= 1
ans += tmp
ans %= mod
print(ans)




