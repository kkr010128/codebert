# セグメント木 最新バージョン
#verify
class SegTree():
    # 1-indexed
    def __init__(self, lists, function, basement):
        self.n = len(lists)
        self.K = (self.n-1).bit_length()
        self.f = function
        self.b = basement
        self.seg = [basement]*(2**(self.K+1)+1)
        X = 2**self.K
        for i, v in enumerate(lists):
            self.seg[i+X] = v
        for i in range(X-1, 0, -1):
            self.seg[i] = self.f(self.seg[i << 1], self.seg[i << 1 | 1])

    def update(self, k, value):
        X = 2**self.K
        k += X
        self.seg[k] = value
        while k:
            k = k >> 1
            self.seg[k] = self.f(self.seg[k << 1], self.seg[(k << 1) | 1])

    def query(self, L, R):
        num = 2**self.K
        L += num
        R += num
        vL = self.b
        vR = self.b
        while L < R:
            if L & 1:
                vL = self.f(vL, self.seg[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.f(self.seg[R], vR)
            L >>= 1
            R >>= 1
        return self.f(vL, vR)

    def find_max_index(self, L, R, X):
        # [L,R)でX以下の物で最大indexを取得
        return self.fMi(L, R, X, 1, 0, 2**self.K)

    def find_min_index(self, L, R, X):
        # [L,R) でX以下の物で最小のindexを取得する
        return self.fmi(L, R, X, 1, 0, 2**self.K)

    def fMi(self, a, b, x, k, l, r):
        if self.seg[k] > x or r <= a or b <= l:
            return -1
        else:
            if k >= 2**self.K:
                return k-2**self.K
            else:
                vr = self.fMi(a, b, x, (k << 1) | 1, (l + r) // 2, r)
                if vr != -1:
                    return vr
                return self.fMi(a, b, x, k << 1, l, (l + r) // 2)

    def fmi(self, a, b, x, k, l, r):
        if self.seg[k] > x or r <= a or b <= l:
            return -1
        else:
            if k >= 2**self.K:
                return k-2**self.K
            else:
                vl = self.fmi(a, b, x, k << 1, l, (l+r)//2)
                if vl != -1:
                    return vl
                return self.fmi(a, b, x, k << 1 | 1, (l+r)//2, r)
N = int(input())
S = list(input())
Q = int(input())
que = [tuple(input().split()) for i in range(Q)]
alpha = "abcdefghijklmnopqrstuvwxyz"
Data = {alpha[i]: [0]*N for i in range(26)}
for i in range(N):
    Data[S[i]][i] += 1
SEG = {alpha[i]: SegTree(Data[alpha[i]], max, 0) for i in range(26)}
for X, u, v in que:
    if X == "1":
        u = int(u)-1
        NOW = S[u]
        S[u] = v
        SEG[NOW].update(u, 0)
        SEG[v].update(u,1)
    else:
        s, t = int(u)-1, int(v)-1
        res = 0
        for j in range(26):
            res += SEG[alpha[j]].query(s, t+1)
        print(res)
