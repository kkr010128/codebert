import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)
from heapq import heappush, heappop

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def rangeI(it, l, r):
    for i, e in enumerate(it):
        if l <= i < r:
            yield e
        elif l >= r:
            break

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

INF = 999999999999999999999999
MOD = 10**9+7

n = int(input())
S = [ input() for _ in range(n)]

left = 0
right = 0

l_ok = [False] * n
r_ok = [False] * n
LMR = [0] * n
MIN_LMR = [0] * n

for i,s in enumerate(S):
    l = 0
    r = 0
    lok = True
    for j,c in enumerate(s):
        if c == "(":
            l += 1
        else:
            r += 1
            if r > l:
                lok = False
        MIN_LMR[i] = min(MIN_LMR[i], l-r)
    LMR[i] = l - r
    l = 0
    r = 0
    rok = True
    for j in range(len(s)-1, -1, -1):
        if s[j] == "(":
            l += 1
            if l > r:
                rok = False
                break
        else:
            r += 1

    left += s.count("(")
    right += s.count(")")

    l_ok[i] = lok
    r_ok[i] = rok

# log(l_ok)
# log(r_ok)

if left != right:
    print("No")
    exit()


positives = [ (MIN_LMR[i], LMR[i]) for i,x in enumerate(LMR) if x > 0 ]
zeros     = [ (MIN_LMR[i], LMR[i]) for i,x in enumerate(LMR) if x == 0 ]
negatives = [ (MIN_LMR[i], LMR[i]) for i,x in enumerate(LMR) if x < 0]
for i in range(len(negatives)):
    min_lmr, lmr = negatives[i]
    min_lmr = min_lmr - lmr
    lmr = -1 * lmr
    negatives[i] = (min_lmr, lmr)

positives.sort(reverse=True)
negatives.sort(reverse=True)

h = 0
for min_lmr, lmr in positives + zeros:
    if h+min_lmr < 0:
        print("No")
        exit()
    h += lmr

h = 0
for min_lmr, lmr in negatives:
    if h+min_lmr < 0:
        print("No")
        exit()
    h += lmr

print("Yes")