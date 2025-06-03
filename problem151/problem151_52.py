N, M, K = list(map(int,input().split()))
m = 998244353

# コンビネーション _{N} C_n (n=1,...,N)をmod mで計算する
# フェルマーの小定理を利用する
# 計算量はO(max(N,m))
class combination_mod: # mod mのもとでのN C nを計算するクラス，計算量はO(N)
    def __init__(self,N,m):
        self.N = N
        self.m = m
        self.N_factorials = [1 for _ in range(N)] # 1!からN!までをmod mで計算したリスト
        for n in range(1,N):
            self.N_factorials[n] = (self.N_factorials[n-1] * (n+1)) % m
        N_factorial_inv = pow(self.N_factorials[N-1], m-2, m) # N!^{-1} = N!^{m-2} (mod m)を計算する，高速
        self.N_factorials_inv = [1 for _ in range(N)] # N!^{-1}から1!^{-1}までをmod mで計算したリスト
        self.N_factorials_inv[0] = N_factorial_inv
        for n in range(1,N): # nは1からN-1まで走る
            self.N_factorials_inv[n] = (self.N_factorials_inv[n-1] * (N-n+1)) % m
    def calc(self,n): # N C n (mod m)を計算する，計算量はO(1)
        if n == 0 or n == self.N:
            return 1
        else:
            c = (self.N_factorials[self.N-1] * self.N_factorials_inv[self.N-n]) % self.m # ここが N! * n!^{-1}
            c = (c * self.N_factorials_inv[n]) % self.m # ここが * (N-n)!^{-1}
            return c
if N == 1:
    print(M%m)
    exit()
elif M == 1:
    if N > K+1:
        print(0)
    else:
        print(1)
    exit()
else:
    func = combination_mod(N-1,m)
    ans = 0
    for k in range(K+1):
        ans_temp = M
        ans_temp = (ans_temp * func.calc(k)) % m
        ans_temp = (ans_temp * pow(M-1,N-1-k,m)) % m
        ans += ans_temp
        ans = ans % m
    print(ans)
