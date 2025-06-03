class SegmentTree():
    """一点更新、区間取得クエリをそれぞれO(logN)で答えるデータ構造を構築する。
    built(array)   := arrayを初期値とするセグメント木を構築する O(N)。
    update(i, val) := i番目の要素をvalに変更する。
    get_val(l, r)  := 区間[l, r)に対する二項演算の畳み込みの結果を返す。
    """
    def __init__(self, n, op, e):
        """要素数、二項演算、単位元を引数として渡す
        例) 区間最小値 SegmentTree(n, min, 10 ** 18)
            区間和     SegmentTree(n, lambda a, b : a + b, 0)
        """
        self.n = n
        self.op = op
        self.e = e
        self.size = 2 ** ((n - 1).bit_length())
        self.node = [self.e] * (2 * self.size)

    def build(self, array):
        """arrayを初期値とするセグメント木を構築する"""
        for i in range(self.n):
            self.node[self.size + i] = array[i]
        for i in range(self.size - 1, 0, -1):
            self.node[i] = self.op(self.node[i << 1], self.node[(i << 1) + 1])

    def update(self, i, val):
        """i番目の要素をvalに変更する"""
        i += self.size
        self.node[i] = val
        while i > 1:
            i >>= 1
            self.node[i] = self.op(self.node[i << 1], self.node[(i << 1) + 1])

    def get_val(self, l, r):
        """[l, r)の畳み込みの結果を返す"""
        l, r = l + self.size, r + self.size
        res_l, res_r = self.e, self.e
        while l < r:
            if l & 1:
                res_l = self.op(res_l, self.node[l])
                l += 1
            if r & 1:
                r -= 1
                res_r = self.op(self.node[r], res_r)
            l, r = l >> 1, r >> 1
        return self.op(res_l, res_r)


ALPH = "abcdefghijklmnopqrstuvwxyz"
to_int = {char: i for i, char in enumerate(ALPH)}


n = int(input())
s = input()
q = int(input())
query = [list(input().split()) for i in range(q)]

init = [0] * n
for i, char in enumerate(s):
    init[i] = 1 << to_int[char]

op = lambda a, b: a | b
st = SegmentTree(n, op, 0)
st.build(init)

for i in range(q):
    if query[i][0] == "1":
        _, ind, char = query[i]
        ind = int(ind) - 1
        st.update(ind, 1 << to_int[char])
    else:
        _, l, r = query[i]
        l, r = int(l) - 1, int(r) 
        print(bin(st.get_val(l, r)).count("1"))
