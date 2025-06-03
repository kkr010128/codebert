N, K = [int(i) for i in input().split()]
mod = 10**9+7
result = 0 
for i in range(K, N+2):
    min_sum = ((i-1) * i) // 2
    max_sum = ((N) * (N+1)) // 2 - ((N-i) * (N-i+1)) // 2
    result += (max_sum - min_sum + 1) % mod
print(result%mod)