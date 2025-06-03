K,N = map(int,input().split())
A = list(map(int,input().split()))

max_range = 0

for i in range(N):
    if i == N-1:
        if max_range < K-A[i]+A[0]:
            max_range = K-A[i]+A[0]
    else:
        if max_range < A[i+1]-A[i]:
            max_range = A[i+1]-A[i]
            

ans = K - max_range
print(ans)