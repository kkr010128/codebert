import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[] for _ in range(num)]
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

H,W,K = II()
s = [str(input()) for _ in range(H)]
ans = [[0]*W for _ in range(H)]

count = 0
no_row = []
for i in range(H):
    p = []
    for j in range(W):
        if s[i][j]=='#':
            p.append(j)
    if len(p):
        count += 1
        for j in range(W):
            if s[i][j] == '#' and j!=p[0]:
                count += 1
            ans[i][j] = count
    else:
        no_row.append(i)

for i in no_row:
    for j in range(W):
        for k in range(i+1,H):
            if ans[k][j]:
                ans[i][j] = ans[k][j]
                break
        for k in range(i)[::-1]:
            if ans[k][j]:
                ans[i][j] = ans[k][j]
                break

for a in ans:
    print(*a)