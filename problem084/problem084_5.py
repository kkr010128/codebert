def resolve():
    import sys
    sys.setrecursionlimit(10 ** 6)  # 再帰関数の再帰の深さを設定
    to_index = lambda x: int(x) - 1  # 入力した数字に1を引いたものを返す
    print_list_in_2D = lambda x: print(*x, sep="\n")  # リストの要素を改行を挟んで表示する関数



    # 入力を整数に変換して受け取る
    def input_int():
        return int(input())

    def map_int_input():
        return map(int, input())

    MII = map_int_input

    def MII_split():
        return map(int, input().split())

    def MII_to_index():
        return map(to_index, input())

    def MII_split_to_index():
        return map(to_index, input().split())

    # 入力全てを整数に変換したものの配列を受け取る
    def list_int_inputs():
        return list(map(int, input()))

    LII = list_int_inputs

    def LII_split():
        return list(map(int, input().split()))

    # 2次元リスト化
    def LII_2D(rows_number):
        return [LII() for _ in range(rows_number)]

    def LII_split_2D(rows_number):
        return [LII_split() for _ in range(rows_number)]

    class UnionFind:
        def __init__(self, n):
            """
            :param n: 人数
            :type n: int
            """
            self.n = n
            self.parents = [-1] * n

        def find(self, x):
            if self.parents[x] < 0:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]

        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)

            if x == y:
                return

            if self.parents[x] > self.parents[y]:
                x, y = y, x

            self.parents[x] += self.parents[y]
            self.parents[y] = x

        def size(self, x):
            return -self.parents[self.find(x)]

        def same(self, x, y):
            return self.find(x) == self.find(y)

        def members(self, x):
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]

        def roots(self):
            return [i for i, x in enumerate(self.parents) if x < 0]

        def group_count(self):
            return len(self.roots())

        def all_group_members(self):
            return {r: self.members(r) for r in self.roots()}

        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    N, M = MII_split()


    # groups = []
    uf = UnionFind(N)

    for _ in range(M):
        A, B = MII_split()
        uf.union(A-1, B-1)  # unionfindを使い、結合の計算量を減らす
        # is_in_groups = False
        # for group in groups:
        #     if A in group and B not in group:
        #         group.append(B)
        #         break
        #     elif B in group and A not in group:
        #         group.append(A)
        #         break
        #     elif A in group and B in group:
        #         is_in_groups = True
        #         break
        # if not is_in_groups:
        #     groups.append([A, B])

    print(max(uf.size(x) for x in range(uf.group_count())))
    
resolve()
