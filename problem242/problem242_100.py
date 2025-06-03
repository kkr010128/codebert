def cmb(a,b,c):
    b = min(b,a-b)
    num = 1
    for i in range(b):
        num = num*(a-i) % c
    den = 1
    for i in range(b):
        den = den*(i+1) % c
    return num * pow(den,c-2,c) % c
mod = 10**9 + 7
n,k = map(int,input().split())
inv = [0,1]
for i in range(2,n):
  inv += [inv[mod % i]*(mod - mod//i) % mod]
a = list(map(int,input().split()))
a.sort()
ans = 0
c = 1
x = 1
if k == 1:
    print(0)
    exit()
for i in range(n-k+1):
    ans -= a[n-k-i] * c
    ans += a[k+i-n-1] * c
    ans %= mod
    c = c*(i+k)*inv[i+1] % mod
if ans < 0:
    ans += mod
print(ans)