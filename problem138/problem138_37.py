import sys
from collections import OrderedDict
input = sys.stdin.readline
sys.setrecursionlimit(2 * 10**6)


def inpl():
    return list(map(int, input().split()))


def main():
    MOD = 998244353
    N, S = inpl()
    A = sorted(inpl())
    dp = {}
    dp[0] = 1
    for i, a in enumerate(A):
        # print(i, dp)
        ks = sorted(dp.keys())
        for k in ks[::-1]:
            # print(k)
            if k + a <= S:
                if k + a in dp:
                    dp[k + a] = (dp[k] + dp[k + a]) % MOD
                else:
                    dp[k + a] = dp[k]
            dp[k] = (dp[k] * 2) % MOD
    # print(dp)
    print(0 if S not in dp else dp[S])
    return


if __name__ == '__main__':
    main()
