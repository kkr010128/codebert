"""D."""

import sys


def input() -> str:  # noqa: A001
    """Input."""
    return sys.stdin.readline()[:-1]


class UnionFindTree:
    """Union-find."""

    def __init__(self, n: int) -> None:
        """Init."""
        self.n = n
        self.rank = [-1] * n

    def find_root(self, x: int) -> int:
        """Find root."""

        if self.rank[x] < 0:
            return x

        self.rank[x] = self.find_root(self.rank[x])
        return self.rank[x]

    def union(self, x: int, y: int) -> None:
        """Unite two trees."""
        x_root = self.find_root(x)
        y_root = self.find_root(y)

        if x_root == y_root:
            return

        if x_root > y_root:
            x_root, y_root = y_root, x_root

        self.rank[x_root] += self.rank[y_root]
        self.rank[y_root] = x_root

    def get_size(self, x: int) -> int:
        """Get size."""
        return self.rank[self.find_root(x)] * -1

    def is_same(self, x: int, y: int) -> bool:
        """Is same group."""
        return self.find_root(x) == self.find_root(y)


n, m = map(int, input().split(' '))

tree = UnionFindTree(n)

for _ in range(m):
    a, b = map(int, input().split(' '))
    tree.union(a - 1, b - 1)

ans = 0

for i in range(n):
    ans = max(ans, tree.get_size(i))

print(ans)
