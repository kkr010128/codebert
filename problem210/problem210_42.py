import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())
ord_a = ord("a")

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

bits = [Bit(N) for _ in range(26)]

for i in range(N):
    s = S[i]
    bits[ord(s) - ord_a].add(i + 1, 1)

Q = int(input())

for _ in range(Q):
    query = input().rstrip().split()
    if query[0] == "1":
        i, c = int(query[1]), query[2]
        bits[ord(S[i - 1]) - ord_a].add(i, -1)
        S[i - 1] = c
        bits[ord(S[i - 1]) - ord_a].add(i, 1)
    else:
        l, r = int(query[1]), int(query[2])
        res = 0
        for bit in bits:
            if l != 1:
                res += int(bit.sum(r) - bit.sum(l - 1) > 0)
            else:
                res += int(bit.sum(r) > 0)
        print(res)