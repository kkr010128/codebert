N, K = map(int, input().split())

mod = 1000000007

ans = 0
for i in range(K, N+1+1):
    num_min = i*(i-1)//2
    num_max = i*(N+N-i+1)//2
#    print(num_min, num_max)
    ans += (num_max - num_min + 1)%mod
print(ans%mod)