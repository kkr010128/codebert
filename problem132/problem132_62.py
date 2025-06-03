from itertools import accumulate
class Imos:
    def __init__(self, n):
        self.A = [0]*(n+1)
        self.n = n

    def __call__(self):
        
        dist = list(accumulate(self.A))[:self.n]
        self.A = [0] * (self.n+1)
        return dist

    def query(self, l, r):
        self.A[l] += 1
        self.A[r] -= 1

n, k, *A = map(int, open(0).read().split())
imos = Imos(n)
for _ in range(min(100, k)):
    for i in range(n):
        imos.query(max(0, i-A[i]), min(i+A[i]+1, n))
    A = imos()
print(*A)