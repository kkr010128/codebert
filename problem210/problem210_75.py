import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self,l):
        nb = bin(len(l))[2:]
        b = sum([int(d) for d in nb])
        if b == 1:
            self.end_leaves = pow(2,len(nb)-1)
        else:
            self.end_leaves = pow(2,len(nb))
        self.tree = [set() for _ in range(self.end_leaves*2)]
        
        for i in range(len(l)):
            self.tree[self.end_leaves+i].add(l[i])
            
    def union(self,a):
        if a >= self.end_leaves // 2:
            self.tree[a] = self.tree[a*2] | self.tree[a*2+1]
            return self.tree[a]
        else:
            self.tree[a] = self.union(a*2) | self.union(a*2+1)
            return self.tree[a]
    def update(self,a,s):
        x = a + self.end_leaves
        if s not in self.tree[x]:
            self.tree[x] = set(s)
            while x > 1:
                x //= 2
                self.tree[x] = self.tree[x*2] | self.tree[x*2+1]
    def query(self,l,r):
        x = l + self.end_leaves
        y = r + self.end_leaves
        tl = set()
        tr = set()
        while y - x > 1:
            if x % 2 == 1:
                tl = tl | self.tree[x]
                x += 1
            if y % 2 == 0:
                tr = self.tree[y] | tr
                y -= 1
            x >>= 1
            y >>= 1
        if y - x == 0:
            print(len(tl|tr|self.tree[x]))
        else:
            print(len(tl|tr|self.tree[x]|self.tree[y]))
            
            

N = int(input())
S = list(input())
st = SegmentTree(S)
st.union(1)
Q = int(input())
for i in range(Q):
    q = input().split()
    if q[0] == '1':
        st.update(int(q[1])-1,q[2])
    else:
        st.query(int(q[1])-1,int(q[2])-1)