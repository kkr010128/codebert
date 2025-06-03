import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N,K = LI()
    f = [1]
    r = [1]

    s = 1
    for i in range(1,N+2):
        s = (s * i) % MOD
        f.append(s)
        r.append(pow(s,MOD-2,MOD))


    def comb(a,b):
        return f[a] * r[b] * r[a-b]

    ans = 0
    for k in range(min(K,N-1)+1):
        ans = (ans + comb(N,k) * comb(N-1,k)) % MOD
    print(ans)

if __name__ == '__main__':
    main()