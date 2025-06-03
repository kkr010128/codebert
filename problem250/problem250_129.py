class PrimeFactor():

    def __init__(self, n):                  # エラトステネス　O(N loglog N)
        self.n = n
        self.table = list(range(n+1))       # 最小素因数のリスト
        self.table[2::2] = [2]*(n//2)
        for p in range(3, int(n**0.5) + 2, 2):
            if self.table[p] == p:
                for q in range(p * p, n + 1, 2 * p):
                    if self.table[q] == q:
                        self.table[q] = p

    def is_prime(self, x):  # 素数判定　O(1)
        if x < 2:
            return False
        return self.table[x] == x

p = PrimeFactor(10**6)

X = int(input())

while True:
    if p.is_prime(X):
        print(X)
        exit()
    else:
        X += 1
