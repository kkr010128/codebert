n = int(input())
l = list(map(int,input().split()))
mod = 10**9+7

ones = [0]*60
ans = 0
for i in range(n):
    x = l[i]
    for j in range(60):
        ones[j] += (x>>j)&1
    ans = (ans + (n-1)*x)%mod
# print(ans)

for i in range(60):
    ans = (ans - ones[i]*(ones[i]-1)*2**i)%mod
print(ans)