# coding: utf-8
import sys
from collections import defaultdict
from math import gcd

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

# 0除算、グループ分け
MOD = 10 ** 9 + 7
N = ir()
AB = [lr() for _ in range(N)]  # 0-indexed
dic = defaultdict(set)
zero = [set() for _ in range(3)]
for i, (a, b) in enumerate(AB, 1):
    g = gcd(a, b)
    #print('g, a, b:', g, a, b)
    if a != 0 and b != 0:
        a //= g; b //= g
        if a < 0:
            a *= -1; b *= -1
        dic[(a, b)].add(i)
    elif a == 0:
        if b == 0:
            zero[0].add(i)
        else:
            zero[1].add(i)
    elif b == 0:
        zero[2].add(i)

answer = 1
used = set()
for k, v in dic.items():
    a, b = k
    k2 = (-b, a)
    if -b < 0:
        k2 = (b, -a)
    if k in used:
        continue
    if k2 in dic:
        v2 = dic[k2]
        answer *= (-1 + pow(2, len(v), MOD) + pow(2, len(v2), MOD))
        used.add((k2))
    else:
        answer *= pow(2, len(v), MOD)
    used.add(k)
    answer %= MOD

# zero
answer *= -1 + pow(2, len(zero[1]), MOD) + pow(2, len(zero[2]), MOD)
answer += len(zero[0])
answer -= 1  # 何も選ばなかった場合
print(answer % MOD)
# np.int64とint型の違いに注意
# 07