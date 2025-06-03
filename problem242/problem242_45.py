import sys
input = sys.stdin.readline

class Combination:                                      # 計算量は O(n_max + log(mod))
    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        f = 1
        self.fac = fac = [f]
        for i in range(1, n_max+1):                     # 階乗(= n_max !)の逆元を生成
            f = f * i % mod                             # 動的計画法による階乗の高速計算
            fac.append(f)                               # fac は階乗のリスト
        f = pow(f, mod-2, mod)                          # 階乗から階乗の逆元を計算。フェルマーの小定理より、　a^-1 = a^(p-2) (mod p) if p = prime number and p and a are coprime
                                                        # python の pow 関数は自動的に mod の下での高速累乗を行ってくれる
        self.facinv = facinv = [f]
        for i in range(n_max, 0, -1):                   # 上記の階乗の逆元から階乗の逆元のリストを生成（＝ facinv ）
            f = f * i % mod
            facinv.append(f)
        facinv.reverse()


    def __call__(self, n, r):  # self.C と同じ
        if not 0 <= r <= n: return 0
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

############################################################################################################
from itertools import combinations

MOD = mod=10**9+7

N, K = map(int, input().split())
C = Combination(N)
A = list(map(int, input().split()))
if K == 1:
    print(0)
    exit()
A.sort()

res = 0
for i in range(K-1,N):
    res += C(i+1-1,K-1) * A[i]

for i in range(N-K+1):
    res -= C(N-i-1,K-1) * A[i]

print(res%MOD)
