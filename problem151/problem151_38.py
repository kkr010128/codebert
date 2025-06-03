def abc167_e():
    N, M, K = map(int, input().split())
    Mod = 998244353

    class CombiMod:
        ''' combination mod prime '''

        def __init__(self, N, Mod):
            ''' 前計算 '''
            self.mod = Mod
            self.fac = [1] * (N+1)  # fac[0] = fac[1] = 1
            for i in range(1, N+1):
                self.fac[i] = (self.fac[i-1] * i) % self.mod
            self.finv = [1] * (N+1)  # finv[0] = finv[1] = 1
            self.finv[N] = pow(self.fac[N], self.mod-2, self.mod)
            for i in range(N, 0, -1):
                self.finv[i-1] = (self.finv[i] * i) % self.mod

        def __call__(self, n: int, k: int):
            ''' nCkを実際に計算する '''
            if k < 0 or n < k: return 0
            ret = self.fac[n] * self.finv[k] % self.mod
            ret = ret * self.finv[n-k] % self.mod
            return ret

    cmb = CombiMod(N, Mod)
    ans = 0

    for x in range(K+1):
        p = cmb(N-1, x) * M * pow(M-1, N-x-1, Mod) % Mod
        ans = (ans + p) % Mod
    print(ans)

abc167_e()