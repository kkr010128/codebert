N = int(input())
A = list(map(int, input().split()))

ans = 1
l = [0] * N
for i in range(N):
  n = A[i]
  if 0 < n:
    ans *= l[n-1] - l[n]
  else:
    ans *= 3 - l[n]
  l[n] += 1
  ans %= 1000000007
print(ans)