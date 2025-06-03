n, m = map(int,input().split())

class unionfind():
    def __init__(self,n):
        self.li = [i for i in range(n+1)]
        self.group = [1]*(n+1)

    def find(self, x):
        while self.li[x]!=x:
            x = self.li[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return;
        elif x>y:
            self.li[y] = x
            self.group[x] += self.group[y]
        else:
            self.li[x] = y
            self.group[y] += self.group[x]
x = unionfind(n)
ans = 0
for _ in range(m):
    a,b = map(int,input().split())
    x.union(a,b)
print(max(x.group))