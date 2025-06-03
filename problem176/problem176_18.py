N,K = map(int,input().split())
mod = 10**9+7
ans = [0]*(K+1)
result = 0

for i in range(K,0,-1):
    c = K//i
    ans[i] += pow(c,N,mod)
    for j in range(i,K+1,i):
        if i != j:
            ans[i] -= ans[j]
    result += i*ans[i] % mod

print(result%mod)