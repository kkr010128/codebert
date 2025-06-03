N, M = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
A = A[::-1]
X = sum(A)
Y = 1/4/M
ans = 'Yes'
for i in range(M):
  if A[i]/X < Y:
    ans = 'No'
print(ans)