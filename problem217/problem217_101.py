N = int(input())
A = list(map(int,input().split()))

ans = "APPROVED"

for n in range(N):
  if A[n] %2 == 0:
    if A[n] % 3 != 0 and A[n] % 5 != 0:
      ans = "DENIED"
      break
print(ans)