import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N,T = LI()
    A = [LI() for _ in range(N)]
    A.sort()
    dp = [[0] * (T+1) for _ in range(N+1)]

    for i in range(1,N+1):
        for j in range(1,T+1):
            a,b = A[i-1]
            if j == T:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+b)
                continue
            if j < a:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-a]+b)
    print(dp[-1][T])


if __name__ == '__main__':
    main()