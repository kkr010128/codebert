N, M = map(int, input().split())
A = list(map(int, input().split()))
 
s = sum(A)
A = sorted(A, reverse=True)
ans = 'Yes'
for i in range(M):
  if A[i]*(4*M) < s: 
    ans = 'No'
    break

print(ans)