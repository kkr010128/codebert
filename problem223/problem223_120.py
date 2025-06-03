N,K = map(int,input().split())
ps = list(map(int,input().split()))
su = sum(ps[0:K])
ksum = su
ind = 0
for i in range(1,N-K+1):
    ksum -= ps[i-1]
    ksum += ps[i+K-1]
    if ksum > su:
        ind = i
        su = ksum
ki = 0

for i in range(ind, ind+K):
    ki += (ps[i]*(ps[i]+1))/2/ps[i]
print(ki)
