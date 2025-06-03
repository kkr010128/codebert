class UnionFind():
    """
        unionfindtree のクラス
            グループを管理するデータ構造.
            全てのメソッドの計算量が O(log(n)) よりも小さい
        init: 管理対象の個数 n を用いて初期化
        find: ある要素 x の親がどの要素か返す
        union: ある要素 x と y が属しているグループを結合して1つのグループとする
        msize: ある要素 x が属するグループの大きさを返す
    """
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n
        self.rank = [0]*n
        self.size = [1]*n

    def find(self, x):
        """
            ある要素 x の親の要素を見つけるメソッド
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        """
            ある要素 x, y の属するグループを結合するメソッド
            x と y のランク(子の数)の小さい方が結合先の親となる
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.size[y] += self.size[x]
            self.parents[x] = y
        else:
            self.size[x] += self.size[y]
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def msize(self, x):
        """
            ある要素 x の属するグループの大きさを返すメソッド
        """
        return self.size[self.find(x)]
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
        return len(self.roots())


def main():
    N, Q = map(int, input().split())
    uf = UnionFind(N)
    for _ in range(Q):
        u, v = map(int, input().split())
        uf.union(u-1, v-1)
    print(uf.group_count()-1)   
if __name__ == "__main__":
    main()
