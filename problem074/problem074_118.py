N,K = map(int,input().split())
l = []
mod = 998244353
for i in range(K):
    L,R = map(int,input().split())
    l.append([L,R])
l.sort()

a = [0 for i in range(N+1)]
a[1] = 1
b = [0 for i in range(N+1)]
b[1] = 1
for i in range(2,N+1):
    for j in range(K):
        if l[j][0] < i:
            a[i] += (b[i-l[j][0]]-b[max(0,i-l[j][1]-1)])%mod
        else:
            break
    b[i] = (b[i-1]+a[i])%mod
mod = 998244353
print(a[N]%mod)