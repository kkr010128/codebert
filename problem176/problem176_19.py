N,K = [int(x) for x in input().split()]
count = [0]*(K+1)
ans = 0
mod = 1000000007
for i in range(K,0,-1):
    kosuu = pow(K//i,N,mod)
    if K // i >= 2:
        for j in range(K//i,1,-1):
            kosuu -= count[j*i]
    ans += i*kosuu
    count[i] = kosuu
print(ans%mod)