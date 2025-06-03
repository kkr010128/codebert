from sys import stdin
import sys
sys.setrecursionlimit(10**7)


def main():
    _in = [_.rstrip() for _ in stdin.readlines()]
    N, K = list(map(int, _in[0].split(' ')))  # type:list(int)
    L_R_arr = []
    for i in range(K):
        _ = list(map(int, _in[i+1].split(' ')))  # type:list(int)
        L_R_arr.append(_)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    dp = [0] * N
    sdp = [0] * (N+1)
    dp[0] = 1
    for i in range(N):
        for L, R in L_R_arr:
            right = max(0, i-L+1)
            left  = max(0, i-R)
            dp[i] += sdp[right] - sdp[left]
        else:
            sdp[i+1] = (sdp[i] + dp[i]) % 998244353
    ans = dp[-1] % 998244353
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(ans)


if __name__ == "__main__":
    main()
