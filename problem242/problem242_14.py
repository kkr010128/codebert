P = 10**9+7
N, K = map(int, input().split())
S = list(map(int, input().split()))
S.sort()
ans = 0
c = 1
for i in range(N-K+1):
    ans += (S[K-1+i]*c)%P
    ans -= (S[N-K-i]*c)%P
    ans %= P
    c = c*(K+i)*pow(i+1, P-2, P)%P
print(ans)