import sys
input = sys.stdin.readline
N = int(input())
S = input().rstrip()
Q = int(input())
qs = [input().split() for i in range(Q)]

class BinaryIndexedTree:
    def __init__(self,size):
        self.N = size
        self.bit = [0]*(size+1)
    def add(self,x,w): # 0-indexed
        x += 1
        while x <= self.N:
            self.bit[x] += w
            x += (x & -x)
    def _sum(self,x): # 1-indexed
        ret = 0
        while x > 0:
            ret += self.bit[x]
            x -= (x & -x)
        return ret
    def sum(self,l,r): # [l,r)
        return self._sum(r) - self._sum(l)
    def __str__(self): # for debug
        arr = [self.sum(i,i+1) for i in range(self.N)]
        return str(arr)

bits = [BinaryIndexedTree(N+1) for i in range(26)]
for i,c in enumerate(S):
    ci = ord(c) - ord('a')
    bits[ci].add(i,1)
now = list(S)

for a,b,c in qs:
    if a=='1':
        b = int(b)
        pi = ord(now[b-1]) - ord('a')
        bits[pi].add(b-1, -1)
        ci = ord(c) - ord('a')
        bits[ci].add(b-1, 1)
        now[b-1] = c
    else:
        b,c = int(b),int(c)
        cnt = 0
        for i in range(26):
            cnt += int(bits[i].sum(b-1,c) > 0)
        print(cnt)