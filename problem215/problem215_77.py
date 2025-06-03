N ,K = map(int, input().split())
MOD = 10**9 + 7
ans = 0

S = [0]*(2*10**5+1)
S[1] = 1
for i in range(2, 2*10**5+1):
    S[i] = S[MOD%i]*(MOD-int(MOD/i))%MOD

if N-1 <= K:
    ans = 1
    num = 2*N - 1
    for i in range(N-1):
        ans *= (num-i)*S[i+1]
        ans %= MOD
    print(ans%MOD)
else:
    S1 = [1]*N
    S2 = [1]*N
    for i in range(1, N):
        S1[i] = (S1[i-1]*(N+1-i)*S[i])%MOD
        S2[i] = (S2[i-1]*(N-i)*S[i])%MOD
    ans = 0
    for i in range(K+1):
        ans += S1[i]*S2[N-1-i]
        ans %= MOD
    print(ans)


# nCm * n-mHm
# nCm * n-1Cn-m-1