# C - Traveling Salesman around Lake
K,N = map(int,input().split())
A = list(map(int,input().split()))
tmp = 0
for i in range(N):
    tmp = max(tmp, (A[i]-A[i-1])%K)
print(K-tmp)