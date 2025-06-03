import sys
input = sys.stdin.readline

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    
    def add(self, i, x):
        i += 1
        
        while i<=self.n:
            self.bit[i] += x
            i += i&(-i)

    def acc(self, i):
        s = 0
        
        while i>0:
            s += self.bit[i]
            i -= i&(-i)
        
        return s

N = int(input())
S = list(input()[:-1])
bits = [BIT(N) for _ in range(26)]

for i in range(N):
    j = ord(S[i])-ord('a')
    bits[j].add(i, 1)

Q = int(input())

for _ in range(Q):
    q = input().split()
    
    if q[0]=='1':
        i, c = int(q[1])-1, q[2]
        j = ord(S[i])-ord('a')
        bits[j].add(i, -1)
        k = ord(c)-ord('a')
        bits[k].add(i, 1)
        S[i] = c
    else:
        l, r = int(q[1])-1, int(q[2])-1
        ans = 0
        
        for i in range(26):
            if bits[i].acc(r+1)-bits[i].acc(l)>0:
                ans += 1
        
        print(ans)