N, *A = map(int, open(0).read().split())

ans = [0] * N
for i in range(N):
    ans[A[i]-1] = i+1 

print(*ans)