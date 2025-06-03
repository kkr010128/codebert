#!/usr/bin/env python3

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
[解法メモ]
各桁(桁数iとする)を10**i mod pの形で持っておく.
それの累積和をとって, 再びmod pをとると, 同じ数のペアの範囲はpの倍数になっていることが分かる.(他の問題でもこの解法あった気がする)
よって, 答えは同じ数のペアの数をすべて足したもの.

pが2や5の場合, *10が付くと必ず割り切れるので注意.
つまり, 1桁目が割り切れたら必ず割り切れる.⇒各桁を見ていってpで割り切れるならそれ以前の数を足せば良い.
(例)p=5, s=100のとき
    1は割り切れないからx
    0は割り切れるからo ⇒ 2桁目なので+2(10,0の場合)
    0は割り切れるからo ⇒ 3桁目なので+3(100,00,0の場合)
    ⇒答えは5
"""

n, p = LI() 
s = list(map(int,list(input())))
t = []
ans = 0
if p == 2 or p == 5:
    for i in range(n):
        if s[i] % p == 0:
            ans += i+1
    print(ans)
    quit()
 
for i in range(n):
    t.append(s[i]*pow(10,n-i-1,p))
t = list(accumulate(t))
u = [i % p for i in t]
u = list(Counter(u).items())
ans = 0
for i,j in u:
    if i == 0:
        ans += j
    if j >= 2:
        ans += j*(j-1) // 2
print(ans)
