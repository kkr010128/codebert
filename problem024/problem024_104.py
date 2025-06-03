
import sys
from sys import stdin
input = stdin.readline

n,k = (int(x) for x in input().split())
w = [int(input()) for i in range(n)]

# 最大積載Pのトラックで何個の荷物を積めるか
def check(P):
    i = 0
    for j in range(k):
        s = 0
        while  s + w[i] <= P:
            s += w[i]
            i += 1
            if i == n:
                return n
    return i

def solve():
    left = 0
    right = 100000 * 10000  #荷物の個数 * 1個当たりの最大重量

    while right - left > 1 :
        mid = (right + left)//2
        v = check(mid)
        if v >= n:
            right = mid
        else:
            left = mid
    return right

print(solve())
