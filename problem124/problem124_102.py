import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    MOD = 10**9 + 7
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    K = NI()
    S = SI()
    LS = len(S)

    f = [0] * (K+LS)
    r = [0] * (K+LS)
    f[0] = 1
    r[0] = 1
    c = 1
    for i in range(1, K + LS):
        c = (c * i) % MOD
        f[i] = c
        r[i] = pow(c, MOD - 2, MOD)

    def comb(n, k):
        return (f[n] * r[k] * r[n - k]) % MOD

    ans = 0
    for i in range(K+1):
        ans = (ans + pow(25,i,MOD) * pow(26,K-i,MOD) * comb(i+LS-1,LS-1)) % MOD
    print(ans)

if __name__ == '__main__':
    main()