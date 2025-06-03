N,M,K = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

a_sum = [0 for i in range(N+1)]
for i in range(N):
    a_sum[i+1] = a_sum[i] + A[i]

b_sum = [0 for i in range(M+1)]
for i in range(M):
    b_sum[i+1] = b_sum[i] + B[i]

ans = 0

for i in range(N+1):
    t = a_sum[i]
    l = 0
    r = len(b_sum)
    while(l+1<r):
        c = (l+r)//2
        if t+b_sum[c]<=K:
            l = c
        else:
            r = c
    if a_sum[i]+b_sum[l]<=K:
        ans = max(ans,i+l)

print(ans)