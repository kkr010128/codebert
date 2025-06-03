class GCD:

    def __init__(self, N, K, MOD):
        self.N = N
        self.K = K
        self.MOD = MOD
        self.gcd_count_list = []
        self.gcd_count_list2 = [0]*self.K
        for d in range(1,self.K+1):
            self.gcd_count_list.append(self.gcd_count(d))
        self.gcd_count2()

    def gcd_count(self, d):
        """  d, 2d, 3d,... の最大公約数を持つ K 以下の整数 N 個の組の数　"""
        return pow(self.K//d,self.N,self.MOD)

    def gcd_count2(self):
        """  dの最大公約数を持つ K 以下の整数 N 個の組の数　"""
        res = []
        i = 1
        while K//i > 0:
            for j in range(K//(i+1)+1,K//i+1):
                self.gcd_count_list2[j-1] = self.gcd_count_list[j-1] \
                - sum(self.gcd_count_list2[j*k-1] for k in range(2, i+1))
            i += 1

    def solve(self):
        return sum(d*self.gcd_count_list2[d-1] for d in range(1,K+1))%MOD

N, K = map(int, input().split())
MOD = 10**9 + 7
g = GCD(N, K, MOD)
print(g.solve())