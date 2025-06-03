# coding:UTF-8
import sys
from math import factorial

MOD = 10 ** 9 + 7
INF = float('inf')

N = int(input())    # 数字
A = list(map(int, input().split()))     # スペース区切り連続数字

m = max(A)
num = [0] * (m + 1)
for a in A:
    num[a] += 1

for a in A:
    if num[a] > 1:
        num[a] = 0
    i = 2
    while a * i <= m:
        num[a * i] = 0
        i += 1

res = 0
for n in num:
    if n != 0:
        res += 1

print("{}".format(res))
