N = int(input())
A = list(map(int, input().split()))

if 0 in A:
  ans = 0
else:
  ans = 1
  max_limit = 10 ** 18
  for i in range(N):
    if ans * A[i] > max_limit:
      ans = -1
      break
    else:
      ans *= A[i]

print(str(ans))