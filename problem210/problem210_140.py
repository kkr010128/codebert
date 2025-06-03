#1indexed
class BIT():
    def __init__(self, n):
        self.size = n
        self.bit = [0] * (n+1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i

n = int(input())
s = input()
q = int(input())

bit = [BIT(n+1) for i in range(26)]
for i in range(n):
    bit[ord(s[i])-97].add(i+1, 1)


s = list(s)
for _ in range(q):
    query, a, b = input().split()
    if query == "1":
        i = int(a)
        c = ord(b)-97
        bit[c].add(i, 1)

        bit[ord(s[i-1])-97].add(i, -1)
        s[i-1] = b
    else:
        ans = 0
        for k in range(26):
            if bit[k].sum(int(b))-bit[k].sum(int(a)-1) >= 1:
                ans += 1
        print(ans)
