import sys

#UnionFindTreeクラスの定義
class UnionFind():
    #クラスコンストラクタ
    #selfはインスタンス自身
    def __init__(self, n):
        #親ノードを-1に初期化する
        self.parents = [-1] * n

    #根を探す（再帰関数）
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    #xとyの木を併合する
    def union(self, x, y):
        #x,yの根をX,Yとする
        X = self.find(x)
        Y = self.find(y)

        #根が同じなら結合済み
        if X == Y:
            return

        #ノード数が多い方をXとする
        if self.parents[X] > self.parents[Y]:
            X, Y = Y, X

        #XにYのノード数を足す
        self.parents[X] += self.parents[Y]
        #Yの根をXとする
        self.parents[Y] = X


N, M = map(int, input().split())
info = [tuple(map(int, s.split())) for s in sys.stdin.readlines()]

#UnionFindインスタンスの生成
uf = UnionFind(N)
for a, b in info:
    #インデックスを調整し、a,bの木を結合
    a -= 1; b -= 1
    uf.union(a, b)

ans = min(uf.parents)

print(-ans)