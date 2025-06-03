s = int(input())

a = [-1]*(s+10)
mod = 10**9 + 7

a[0] = 1
a[1] = 0
a[2] = 0
a[3] = 1
if s > 3:
    for i in range (4,s+1):
        a[i] = (a[i-1]+a[i-3])%mod

print(a[s])
