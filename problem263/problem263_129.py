n = int(input())
a = list(map(int, input().split()))
m = 65 # a<2**m
mod = 10**9+7

xor_num = [0]*m
for i in range(n):
    for j in range(m):
        if ((a[i] >> j) & 1):
            xor_num[j] += 1

b = 1
ans = 0
for i in range(m):
    ans += b*xor_num[i]*(n-xor_num[i])
    b *= 2
    b %= mod
print(ans%mod)
