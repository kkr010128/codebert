import sys
def input(): return sys.stdin.readline().strip()
from functools import lru_cache
sys.setrecursionlimit(10**9)
mod = 998244353

def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    """
    再帰の計算式自体は合っていた！
    メモ化再帰とdpで計算量は変わらないはずだが、取りあえずdpで書き直してみる。
    """

    dp = [[0] * (S + 1) for _ in range(N)] # dp[n][s] = (N=n, S=sに対する問題の解)
    dp[0][0] = 1
    for n in range(1, N): dp[n][0] = (dp[n - 1][0] * 2 + 1) % mod
    for s in range(1, S + 1): dp[0][s] = 1 if s == A[0] else 0
    for n in range(1, N):
        for s in range(1, S + 1):
            dp[n][s] = (dp[n - 1][s] * 2 + dp[n - 1][s - A[n]]) if s >= A[n] else dp[n - 1][s] * 2
            if A[n] == s: dp[n][s] += 1
            dp[n][s] %= mod
    print(dp[N - 1][S])

    

if __name__ == "__main__":
    main()
