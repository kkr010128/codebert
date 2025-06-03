def su(n):
    if n < 0:
        return 0
    return n*(n+1)//2
MOD = 10 ** 9 + 7
N, K = map(int, input().split())
num = [i for i in range(N+1)]
ans = 0
su_N = su(N)
for i in range(K, N+2):
    min = su(i-1)
    max = su_N - su(N-i)
    ans += max - min + 1
    ans %= MOD
print(ans)