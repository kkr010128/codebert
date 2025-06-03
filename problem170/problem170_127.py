N,K = map(int,input().split())
min = 0
max = 0
ans = 0
for i in range(K,N+2):
    min = i*(i-1)//2
    max = i*(2*N-i+1)//2
    ans += max-min+1
    ans %= (10**9+7)

print(int(ans))
