N, K = list(map(int, input().split()))

ans = 0
all_sum = N*(N+1)/2

mod = 10**9+7

for i in range(K,N+2):
    min_val = i*(i-1)/2
    max_val = N*(N+1)/2 - (N-i+1)*(N-i)/2
    ans += (int(max_val) - int(min_val) + 1) % mod

#    print(i, min_val, max_val)                                                                        


print(ans%mod)





