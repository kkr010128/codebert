import sys
input = sys.stdin.readline

class UnionFind():
    def __init__(self, n):
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
            return -self.parents[self.find(x)]

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return -self.parents[self.find(x)]

def main():
    N, M = map(int, input().split())
    uf = UnionFind(N+1)
    ans = 1
    if M == 0:
        print(ans)
        return

    for i in range(M):
        x, y = map(int, input().split())
        ans = max(uf.union(x,y), ans)
    print(ans)

if __name__ == '__main__':
    main()