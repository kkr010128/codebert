K,N,*A = map(int, open(0).read().split())

ans = []
for i in range(N-1):
    ans.append(abs(A[i+1] - A[i]))

ans.append(A[0] + K - A[-1])
ans.sort()
ans.pop()

print(sum(ans))