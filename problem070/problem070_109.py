#!/usr/bin/env python3
class UnionFind:
    """Union-Find(素集合データ構造)"""
    def __init__(self, n: int):
        """
        Constructer(Initialize parameter in this class)

        Parameters
        ----------
        n : int
            Number of node
        
        Yields
        -----
        root : list
            When value is postive, express root of the node.
            When it is negative, express this node is root and size of set.
        """

        self.root = [-1] * n

    def find(self, x: int):
        """
        Search root of node x

        Parameters
        ----------
        x : int
            node x

        Returns
        -------
        x : int
            Root of node x
        """

        if self.root[x] < 0:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def unite(self, x: int, y: int):
        """
        Unite two set including node x and node y into one set.

        Parameters
        ----------
        x, y : int
            Node number

        Returns
        -------
        unite_result : bool
            False : Already two node include same set.
            True  : United
        """

        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.root[x] > self.root[y]:
            x, y = y, x
        self.root[x] += self.root[y]
        self.root[y] = x
        return True

    def same(self, x: int, y: int):
        """
        Determine if x and y are in same set.

        Parameters
        ----------
        x, y : int
            Node number

        Returns
        -------
        result : bool
            Determining result
        """

        return self.find(x) == self.find(y)
    
    def size(self, x: int) -> bool:
        """
        Return size of set including node x.

        Parameters
        ----------
        x : int
            Node number

        Returns
        -------
        Size of set : int
        """

        return self.root[self.find(x)] * -1


def main():
    N, M = map(int, input().split())

    lst = UnionFind(N)
    for _ in range(M):
        a, b = map(int, input().split())
        lst.unite(a - 1, b - 1)

    ans = -1
    for i in lst.root:
        if i < 0:
            ans += 1
    print(ans)
    # print(lst.root)


if __name__ == '__main__':
    main()
