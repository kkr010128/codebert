class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(self.n+1) # 1-indexed

    def init(self, init_val):
        for i, v in enumerate(init_val):
            self.add(i, v)

    def add(self, i, x):
        # i: 0-indexed
        i += 1 # to 1-indexed
        while i <= self.n:
            self.bit[i] += x
            i += (i & -i)

    def sum(self, i, j):
        # return sum of [i, j)
        # i, j: 0-indexed
        return self._sum(j) - self._sum(i)

    def _sum(self, i):
        # return sum of [0, i)
        # i: 0-indexed
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & (-i)
        return res

class RangeAddBIT:
    def __init__(self, n):
        self.n = n
        self.bit1 = BIT(n)
        self.bit2 = BIT(n)

    def init(self, init_val):
        self.bit2.init(init_val)

    def add(self, l, r, x):
        # add x to [l, r)
        # l, r: 0-indexed
        self.bit1.add(l, x)
        self.bit1.add(r, -x)
        self.bit2.add(l, -x*l)
        self.bit2.add(r, x*r)

    def sum(self, l, r):
        # return sum of [l, r)
        # l, r: 0-indexed
        return self._sum(r) - self._sum(l)

    def _sum(self, i):
        # return sum of [0, i)
        # i: 0-indexed
        return self.bit1._sum(i)*i + self.bit2._sum(i)

import sys
import io, os
#input = sys.stdin.buffer.readline
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def main():
    n, d, a = map(int, input().split())
    XH = []
    for i in range(n):
        x, h = map(int, input().split())
        XH.append((x-d, h))
    XH.sort()
    X = []
    H = []
    for x, h in XH:
        X.append(x)
        H.append(h)

    bit = RangeAddBIT(n+1)
    bit.init(H)
    import bisect
    ans = 0
    for i in range(n):
        h = bit.sum(i, i+1)
        if h > 0:
            q = (h+a-1)//a
            ans += q
            j = bisect.bisect_right(X, X[i]+2*d)
            bit.add(i, j, -q*a)
    print(ans)

if __name__ == '__main__':
    main()
