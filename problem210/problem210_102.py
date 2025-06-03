class SegmentTree(object):
    """
    セグメントツリー (0-indexed)

    1. 値の更新 O(logN)
    2. 区間クエリ O(logN)
    """
    def __BinOp(self, x, y):
        """ セグ木で使用する二項演算 """
        return x | y

    def __init__(self, init_ele, N:int):
        """
        セグ木を構築する

        init_ele: 単位元 
        N: 要素数
        """
        self.__init_ele = init_ele
        self.__n = 1
        while self.__n < N:
            self.__n <<= 1

        self.__dat = [init_ele] * (2 * self.__n)
    
    def update(self, k:int, x):
        """ k番目の値をxに変更する """
        k += self.__n - 1
        self.__dat[k] = x
        while k:
            k = (k - 1) // 2
            self.__dat[k] = self.__BinOp(
                self.__dat[k * 2 + 1], self.__dat[k * 2 + 2]
                )
    
    def query(self, p:int, q:int):
        """ 区間クエリ [p,q) """
        if q <= p: return self.__init_ele
        p += self.__n - 1
        q += self.__n - 2
        res = self.__init_ele
        while q - p > 1:
            if not (p & 1):
                res = self.__BinOp(res, self.__dat[p])
            if q & 1:
                res = self.__BinOp(res, self.__dat[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        res = self.__BinOp(res, self.__dat[p])
        if p != q: res = self.__BinOp(res, self.__dat[q])
        return res
    
    def get_num(self, k:int):
        """ k番目の値を取得する """
        k += self.__n - 1
        return self.__dat[k]

############################################################
N = int(input())

ST = SegmentTree(0, N)
for i, s in enumerate(list(input())):
    ST.update(i, 1 << (ord(s) - ord('a')))

Q = int(input())
for _ in range(Q):
    x,y,z = map(str,input().split())
    x = int(x); y = int(y)
    if x == 1:
        ST.update(y - 1, 1 << (ord(z) - ord('a')))
    else:
        z = int(z)
        print(bin(ST.query(y - 1, z)).count("1"))