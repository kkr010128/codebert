N,K = map(int,input().split())

# from scipy.special import comb
# a = comb(n, r)

MOD = 10**9 + 7
ans = 0
for k in range(K,N+2):
    # print(k)
    right = (N+N-k+1)*k // 2
    left = (k-1)*k // 2 
    ans += right - left + 1
    ans %= MOD
    # print(ans)
    # ans += comb(N+1, k, exact=True)
    # print(ans)


print(ans)