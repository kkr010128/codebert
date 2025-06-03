import sys
import itertools


class UnionFindTree:
    def __init__(self, n: int) -> None:
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def resolve(in_):
    N, M = map(int, next(in_).split())
    tree = UnionFindTree(N + 1)
    AB = (map(int, line.split()) for line in itertools.islice(in_, M))
    for a, b in AB:
        tree.unite(a, b)
    
    ans = len(frozenset(tree.find(x) for x in range(1, N + 1))) - 1
    return ans


def main():
    ans = resolve(sys.stdin.buffer)
    print(ans)


if __name__ == '__main__':
    main()
