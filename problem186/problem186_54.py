K,N = map(int,input().split())
A = list(map(int,input().split()))
d = []
m = 0
for i in range(1,N):
    m = max(m,A[i]-A[i-1])
ans = K-max(m,(K-A[-1]+A[0]))
print(ans)