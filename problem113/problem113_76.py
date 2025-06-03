import sys
from time import time
from random import randrange, random
input = lambda: sys.stdin.buffer.readline()

DEBUG_MODE = False

st = time()
def get_time():
    return time() - st

L = 26
D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]

ans = [randrange(L) for _ in range(D)]

class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (self.n+1)
    
    def sum(self, i):
        res = 0
        while i > 0:
            res += self.data[i]
            i -= i & -i
        return res
    
    def add(self, i, x):
        if i <= 0: raise IndexError
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    
    def lower_bound(self, x):
        if x <= 0: return 0
        cur, s, k = 0, 0, 1 << (self.n.bit_length()-1)
        while k:
            nxt = cur + k 
            if nxt <= self.n and s + self.data[nxt] < x:
                s += self.data[nxt]
                cur = nxt
            k >>= 1
        return cur + 1

def rsum(x):
    return x*(x+1)//2

b = [BinaryIndexedTree(D) for _ in range(L)]

score = 0
for d, cont in enumerate(ans):
    b[cont].add(d+1, 1)
    score += S[d][cont]

for i in range(L):
    m = b[i].sum(D)
    tmp = 0
    s = [0]
    for j in range(1, m+1):
        s.append(b[i].lower_bound(j))
    s.append(D+1)

    for j in range(len(s)-1):
        x = s[j+1] - s[j] - 1
        tmp += rsum(x)
    
    score -= tmp*C[i]

def chg(d, p, q):
    diff = 0
    d += 1

    o = b[p].sum(d)
    d1 = b[p].lower_bound(o-1)
    d2 = b[p].lower_bound(o+1)

    diff += rsum(d-d1) * C[p]
    diff += rsum(d2-d) * C[p]
    diff -= rsum(d2-d1) * C[p]

    o = b[q].sum(d)
    d1 = b[q].lower_bound(o)
    d2 = b[q].lower_bound(o+1)

    diff += rsum(d2-d1) * C[q]
    diff -= rsum(d-d1) * C[q]
    diff -= rsum(d2-d) * C[q]

    d -= 1
    diff -= S[d][p]
    diff += S[d][q] 

    ans[d] = q
    b[p].add(d+1, -1)
    b[q].add(d+1, 1)
    
    return diff

while True:
    if random() >= 0.8:
        d, q = randrange(D), randrange(L)
        p = ans[d]
        diff = chg(d, p, q)
        if diff > 0:
            score += diff
        else:
            chg(d, q, p)
    else:
        d1 = randrange(D-1)
        d2 = randrange(d1+1, min(d1+3, D))
        p, q = ans[d1], ans[d2]
        diff = chg(d1, p, q)
        diff += chg(d2, q, p)
        if diff > 0:
            score += diff
        else:
            chg(d1, q, p)
            chg(d2, p, q)

    if DEBUG_MODE: print(score)
    if get_time() >= 1.7: break

if DEBUG_MODE: print(score)
else:
    for x in ans: print(x+1)
