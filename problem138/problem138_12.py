import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 998244353
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()

    N,S = LI()
    A = [0] + LI()
    dp = [[0] * (S+1) for _ in range(N+1)]
    dp[0][0] = pow(2,N,MOD)
    d2 = pow(2,MOD-2,MOD)
    for i in range(1,N+1):
        for j in range(0,S+1):
            if j >= A[i]:
                dp[i][j] = (dp[i-1][j] + dp[i-1][j-A[i]] * d2) % MOD
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[-1][-1])

if __name__ == '__main__':
    main()