from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

h,w,k = inpl()
s = [list(input()) for _ in range(h)]
res = INF
for yoko in itertools.product([0,1], repeat=(h-1)):
    # 0:uncut 1:cut
    ln = sum(yoko)
    gr = [[] for _ in range(ln+1)] 
    gr[0].append(0)
    ind = 0
    for i in range(1,h):
        if yoko[i-1]: ind += 1
        gr[ind].append(i)
    possible = True
    for x in range(w):
        for ind in range(ln+1):
            cnt = 0
            for y in gr[ind]:
                if s[y][x] == '1':
                    cnt += 1
            if cnt > k:
                possible = False
                break
        if not possible:
            break
    else:
        cutcnt = 0
        now = [0] * (ln+1)
        for x in range(w):
            for ind in range(ln+1):
                for y in gr[ind]:
                    if s[y][x] == '1':
                        now[ind] += 1
            if max(now) > k:
                now = [0] * (ln+1)
                cutcnt += 1
                for ind in range(ln+1):
                    for y in gr[ind]:
                        if s[y][x] == '1':
                            now[ind] += 1
        res = min(res, cutcnt + ln)
print(res)