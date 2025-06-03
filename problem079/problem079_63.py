s = int(input())
mod = 10**9 + 7

f = [0]*2001
g = [0]*2001

f[3]=1
f[4]=1
g[3]=1
g[4]=2

for i in range(4,s+1):
    f[i]=1 + g[i-3]
    f[i]%=mod
    g[i]=f[i] + g[i-1]
    g[i]%=mod
print(f[s])