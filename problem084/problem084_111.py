import sys
sys.setrecursionlimit(10000000)

class Graph:
    def __init__(self,n,side):
        self.side = side
        self.neighbor = [set() for i in range(n+1)]
        self.visited = [False]*(n+1)
        self.group =[0]*n
        self.product()
    def product(self):
        for a,b in self.side:
            self.neighbor[a].add(b)
            self.neighbor[b].add(a)
    def dfs(self,x,a):
        self.group[a] += 1
        self.visited[x] = True
        for i in self.neighbor[x]:
            if self.visited[i]:continue
            self.dfs(i,a)
    def all_dfs(self):
        a = 0
        for i in range(1,n+1):
            if not self.visited[i]:
                self.dfs(i,a)
                a += 1

n,m = map(int,input().split())
side = list(tuple(map(int,input().split()))for i in range(m))
graph1 = Graph(n,side)
graph1.all_dfs()
print(max(graph1.group))
