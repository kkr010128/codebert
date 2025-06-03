k,n = map(int, input().split())
A = list(map(int, input().split()))
ans = 10**6
for i in range(n-1):
  if ans > k - (A[i+1] - A[i]):
    ans = k - (A[i+1] - A[i])
if ans > A[-1] - A[0]:
  ans = A[-1] - A[0]
print(ans)