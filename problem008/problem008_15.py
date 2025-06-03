# http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=4647653#1



import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

class Graph:
    def __init__(self, n, dictated=False, decrement=True, edge=[]):
        self.n = n
        self.dictated = dictated
        self.decrement = decrement
        self.edge = [set() for _ in range(self.n)]
        self.parent = [-1]*self.n
        self.info = [-1]*self.n
        for x, y in edge:
            self.add_edge(x,y)

    def add_edge(self,x,y):
        if self.decrement:
            x -= 1
            y -= 1
        self.edge[x].add(y)
        if self.dictated == False:
            self.edge[y].add(x)

    def add_adjacent_list(self,i,adjacent_list):
        if self.decrement:
            self.edge[i] = set(map(lambda x:x-1, adjacent_list))
        else:
            self.edge[i] = set(adjacent_list)

    def path_detector(self, start=0, time=0):
        """
        :param p: スタート地点
        :return: 各点までの距離と何番目に発見したかを返す
        """

        edge2= []
        for i in range(self.n):
            edge2.append(sorted(self.edge[i], reverse=True))

        p, t = start, time
        self.parent[p] = -2
        full_path = [(p + self.decrement,t)]
        while True:
            if edge2[p]:
                q = edge2[p].pop()
                if q == self.parent[p] and not self.dictated:
                    """ 逆流した時の処理 """
                    """"""""""""""""""""
                    continue
                if self.parent[q] != -1:
                    """ サイクルで同一点を訪れた時の処理 """
                    """"""""""""""""""""
                    continue
                self.parent[q] = p
                p, t = q, t + 1
                full_path.append((p + self.decrement, t))
            else:
                """ 探索完了時の処理 """
                full_path.append((p + self.decrement, t))
                """"""""""""""""""""
                if p == start and t == time:
                    break
                p, t = self.parent[p], t-1
                """ 二度目に訪問時の処理 """
                """"""""""""""""""""
        return full_path

    def path_list(self):
        """
        :return: 探索経路を返す。
        """
        self.parent = [-1]*self.n
        res = []
        for p in range(self.n):
            if self.parent[p] == -1:
                res.append(self.path_detector(start=p, time=1))
        return res

    def draw(self):
        """
        :return: グラフを可視化
        """
        import matplotlib.pyplot as plt
        import networkx as nx

        if self.dictated:
            G = nx.DiGraph()
        else:
            G = nx.Graph()
        for x in range(self.n):
            for y in self.edge[x]:
                G.add_edge(x + self.decrement, y + self.decrement)
        nx.draw_networkx(G)
        plt.show()

def make_graph(dictated=False, decrement=True):
    """
    自己ループの無いグラフを生成。N>=2
    :param dictated: True = 有効グラフ
    :param decrement: True = 1-indexed
    :return:
    """
    import random
    N = random.randint(2, 5)
    if N > 2:
        M_max = (3*N-6)*(1+dictated)
    else:
        M_max = 1
    graph = Graph(N, dictated, decrement)
    for _ in range(random.randint(0,M_max)):
        graph.add_edge(*random.sample(range(decrement, N+decrement), 2))
    return graph

##################################################################
# 入力が隣接リストの場合
##################################################################

N = int(input())  # 頂点数

graph = Graph(N,dictated=True, decrement=True)

for i in range(N):  # [[頂点1と連結している頂点の集合], [頂点2と連結している頂点の集合],...]
    points = list(map(int, input().split()))[2:]
    graph.add_adjacent_list(i, points)


data = graph.path_list()

from itertools import chain
data = list(chain.from_iterable(data))

res = [[i+1,0,0] for i in range(N)]
for time, a in enumerate(data, start=1):
    i = a[0] - 1
    if res[i][1]:
        res[i][2] = time
    else:
        res[i][1] = time

for a in res:
    print(*a)
