n,m = map(int,input().split())
A = list(map(int,input().split()))
judge = sum(A) / (4 * m)
ans = []
for i in range(n):
  if A[i] < judge :
    continue
  else:
    ans.append(A[i])
print("Yes") if len(ans) >= m else print("No")