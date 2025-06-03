n = int(input())
a = [int(i) for i in input().split()]
cnt = [0]*(n+1)
cnt[-1] = 3
mod = 1000000007
ans = 1
for i in range(n):
    ans *= cnt[a[i]-1]
    ans %= mod
    cnt[a[i]-1] -= 1
    cnt[a[i]] += 1
print(ans)