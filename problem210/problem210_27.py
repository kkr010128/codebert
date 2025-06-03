class BIT:
    def __init__(self, n):
        self.node = [ 0 for _ in range(n+1) ]

    def add(self, idx, w):
        i = idx
        while i < len(self.node) - 1:
            self.node[i] += w
            i |= (i + 1)

    def sum_(self, idx):
        ret, i = 0, idx-1
        while i >= 0:
            ret += self.node[i]
            i = (i & (i + 1)) - 1
        return ret

    def sum(self, l, r):
        return self.sum_(r) - self.sum_(l)


n = int(input())
s = list(input())
q = int(input())

tree = [ BIT(n) for _ in range(26) ]
for i in range(n):
    tree_id = ord(s[i]) - ord("a")
    tree[tree_id].add(i, 1)

for _ in range(q):
    query = input().split()
    com = int(query[0])
    if com == 1:
        idx, new_char = int(query[1]), query[2]
        idx -= 1
        old_char = s[idx]
        new_id = ord(new_char) - ord("a")
        old_id = ord(old_char) - ord("a")

        tree[old_id].add(idx, -1)
        tree[new_id].add(idx, 1)
        s[idx] = new_char

    if com == 2:
        l, r = int(query[1]), int(query[2])
        ret = 0
        for c in range(26):
            if tree[c].sum(l-1, r) > 0:
                ret += 1
        print(ret)