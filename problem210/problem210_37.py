n=int(input())
s=input()
q=int(input())

query=[]
for i in range(q):
    query.append(input())

ide_ele = set()

def segfunc(x, y):
    return x | y

class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        # param k: index(0-index)
        # param x: update value
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1
    def query(self, l, r):
        #[l, r)segfunc, 0-index
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

al = [{s[i]} for i in range(n)]
seg = SegTree(al, segfunc, ide_ele)

for q in query:
    que,a,b=q.split()

    if que == "1":
        seg.update(int(a)-1,set(b))
    else:
        ret=seg.query(int(a)-1,int(b))
        print(len(ret))