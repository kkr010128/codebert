from collections import Counter


def read():
    N, K = list(map(int, input().strip().split()))
    return N, K


def n_gcd(k, N, K, cache, MOD=10**9+7):
    if cache[k] != -1:
        return cache[k]
    n = pow(K // k, N, MOD)
    for j in range(2*k, K+1, k):
        n -= n_gcd(j, N, K, cache)
        n %= MOD
    cache[k] = n
    return n


def solve(N, K, MOD=10**9+7):
    cache = [-1 for k in range(K+1)]
    ans = 0
    for k in range(K, 0, -1):
        ans += n_gcd(k, N, K, cache) * k
        ans %= MOD
    return ans

if __name__ == '__main__':
    inputs = read()
    print("{}".format(solve(*inputs)))
