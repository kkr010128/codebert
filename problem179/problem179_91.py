N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
th = sum(A)/(4*M)

for i in range(len(A)):
  if A[i] >= th:
    cnt += 1

ans = 'Yes' if cnt >= M else 'No'
print(ans)