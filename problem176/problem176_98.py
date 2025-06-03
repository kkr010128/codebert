N,K = list(map(int,input().split()))

MOD = 10**9+7
arr = [pow(K//i, N, MOD) for i in range(1,K+1)]

for i in range(K//2,0,-1):
    arr[i-1] -= sum(arr[2*i-1:K:i]) % MOD
    arr[i-1] %= MOD
    
arr = [(i+1)*j%MOD for i,j in enumerate(arr)]

print(sum(arr)%MOD)