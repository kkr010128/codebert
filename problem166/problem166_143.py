MOD = 2019

def solve(S):
    N = len(S)
    dp = [0 for _ in range(MOD)]
    tmp = 0
    ret = 0
    for i in range(N - 1, -1, -1):
        m = (tmp + int(S[i]) * pow(10, N - i - 1, MOD)) % MOD
        ret += dp[m]
        dp[m] += 1
        tmp = m
    ret += dp[0]
    return ret

if __name__ == "__main__":
    S = input()
    print(solve(S))