from collections import defaultdict 
import sys
input = sys.stdin.readline
from math import gcd

MOD = 1000000007

dic1 = defaultdict(int)

All_zero = 0

S = set()
N = int(input())
ans = 0 #仲が悪い数を数える
for i in range(N):
    a, b = map(int, input().split())
    if a == 0 and b == 0: #なんでもOK
        All_zero += 1
    elif a == 0:
        S.add((0, 1))
        dic1[(0, 1)] += 1
    elif b == 0:
        S.add((1, 0))
        dic1[(1, 0)] += 1
    else:
        GCD = gcd(a, b)
        a //= GCD
        b //= GCD
        if a < 0: #aを必ず正にする
            a *= -1
            b *= -1
        S.add((a, b))
        dic1[(a, b)] += 1
        
lst = []
for a, b in S:
    tmp11 = dic1[(a, b)]
    A = a
    B = b
    if B <= 0:
        B *= -1
        A *= -1
    tmp2 = dic1[(B, -A)]
    # print (a, b, A, B)
    dic1[(B, -A)] = 0
    if tmp11 > 0:
        lst.append((tmp11, tmp2))

# print (lst)

ans = 1
for a, b in lst:
    tmp = (pow(2, a, MOD) - 1) + (pow(2, b, MOD) - 1) + 1 #左側を入れる、右側を入れる、両方入れない
    ans *= tmp
    ans %= MOD

ans = (ans - 1 + All_zero) % MOD
print (ans % MOD)

# print (S)