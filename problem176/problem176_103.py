
def resolve():
    MOD = 10**9+7
    N, K = map(int, input().split())
    cnt = [0]*(K+1)

    for g in range(K, 0, -1):
        cnt[g] = pow(K//g, N, MOD) # (K//g)**N
        gg = g*2
        while gg <= K:
            cnt[g] -= cnt[gg]
            gg += g
    ans = 0
    for g in range(1, K+1):
        ans += cnt[g] * g
        ans %= MOD
    print(ans)    

if __name__ == "__main__":
    resolve()