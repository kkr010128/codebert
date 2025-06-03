#atcoder template
def main():
    import sys
    imput = sys.stdin.readline
    #ここにコード
    #input
    N, M, K = map(int, input().split())

    #output
    mod = 998244353

    n_ = 4*10**5 + 5
    fun = [1]*(n_+1)
    for i in range(1,n_+1):
        fun[i] = fun[i-1]*i%mod
    rev = [1]*(n_+1)
    rev[n_] = pow(fun[n_],mod-2,mod)
    for i in range(n_-1,0,-1):
        rev[i] = rev[i+1]*(i+1)%mod
    def cmb(n,r):
        if n <= 0 or r < 0 or r > n: return 0
        return fun[n]*rev[r]%mod*rev[n-r]%mod

    answer = 0
    for i in range(K+1):
        answer += M*pow(M-1, N-(i+1), mod)*cmb(N-1, i) % mod

    answer %= mod

    if N == 1:
        print(M)
        exit()

    print(answer)
    

if __name__ == "__main__":
    main()