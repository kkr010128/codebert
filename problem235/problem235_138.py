from fractions import gcd
n = int(input())
a = list(map(int, input().split()))

mod = 1000000007

l = 1

for i in range(n):
    l = l * a[i] // gcd(l, a[i])

ans = 0
for i in range(n):
    ans += l // a[i]

print(ans % mod)