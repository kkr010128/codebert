n,k = map(int,input().split())
p = list(map(int,input().split()))
ps = [p[0]] + [0]*(n-1)
for i in range(1,n):
    ps[i] = ps[i-1] + p[i]
maxs = ps[k-1]
for i in range(1,n-k+1):
    maxs = max(maxs,ps[i+k-1]-ps[i-1])

print((maxs+k)/2)