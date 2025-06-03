class BinaryIndexedTree():
    def __init__(self, max_n):
        self.size = max_n + 1
        self.tree = [0] * self.size
        self.depth = self.size.bit_length()
 
    def initialize(self, seq):
        for i, x in enumerate(seq[1:], 1):
            self.tree[i] += x
            j = i + (i & (-i))
            if j < self.size:
                self.tree[j] += self.tree[i]
 
    def __repr__(self):
        return self.tree.__repr__()
 
    def get_sum(self, i):
        s = 0
        while i:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i < self.size:
            self.tree[i] += x
            i += i & -i
 
    def find_kth_element(self, k):
        x, sx = 0, 0
        dx = (1 << self.depth)
        for i in range(self.depth - 1, -1, -1):
            dx = (1 << i)
            if x + dx >= self.size:
                continue
            y = x + dx
            sy = sx + self.tree[y]
            if sy < k:
                x, sx = y, sy
        return x + 1



n = int(input())
s = ["!"]+list(input())
q = int(input())
bit = [BinaryIndexedTree(n+1) for i in range(26)]

for i in range(n):
    ind = ord(s[i+1])-97
    bit[ind].add(i+1,1)

for i in range(q):
    a,b,c = input().split()
    b = int(b)
    if a == "1":
        ind = ord(s[b])-97
        bit[ind].add(b,-1)
        ind = ord(c)-97
        bit[ind].add(b,1)
        s[b] = c
    else:
        ans = 0
        c = int(c)
        for i in range(26):
            if bit[i].get_sum(c)-bit[i].get_sum(b-1):
                ans += 1
        print(ans)