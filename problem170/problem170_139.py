MOD = 10 ** 9 + 7
n, k = map(int ,input().split())
mn = 0
mx = 0
for i in range(k):
    mn += i
    mx += (n-i)
ans = 0
for i in range(k,n+2):
    ans += mx - mn + 1
    ans %= MOD
    mn += i
    mx += (n-i)
print(ans)
