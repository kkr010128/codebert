N, K = map(int, input().split())

MOD = 10**9 + 7
ans = 0
# 選ぶ個数で場合分け
# 選べる個数はK,K+1,K+2,...,N+1

# 等差数列の和S
# 項数n, 初項a,末項l,公差d
# S=(n/2)*(a+l)
# S=(n/2)*{2a+(n-1)d}

for i in range(K, N + 2):
    min_sum = i * (i - 1) // 2  # 0+1+...(項数=i)
    max_sum = (2 * N - i + 1) * i // 2  # N+(N-1)+...(項数=i)
    ans += max_sum - min_sum + 1  # minとmaxの間の数を全て取れる
    ans %= MOD

print(ans)
