N,K = map(int, input().split())
L,R = [0]*K, [0]*K

count = 0
for _ in range(K):
    a,b = map(int, input().split())
    for _1 in range(_):
        x,y = L[_1],R[_1]
        if x <= a <= y or x <= b <= y :
            L[_1] = min(a,x)
            R[_1] = max(b,y)
            break
    else:
        L[_],R[_] =a,b
        count += 1
L,R = L[0:count+1],R[0:count+1]

MOD = 998244353
dp = [0]*(4*10**5+100)
for l, r in zip(L, R):
    dp[min(N + 1, 1 + l)] += 1
    dp[min(N + 1, 1 + r + 1)] -= 1

for i in range(2,N+1):
    number = dp[i-1] + dp[i]
    if number > MOD:
        number -= MOD
    dp[i] = number
    for l, r in zip(L,R):
        dp[i + l] += number
        dp[i + l] %= MOD
        dp[i + r +1] -= number
        dp[i + r +1] %= MOD

print(dp[N]%MOD)