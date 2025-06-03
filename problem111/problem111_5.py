def solve():
  N = int(input())
  A = list(map(int, input().split()))
  A.sort(reverse=True)
  ans = A[0]
  cnt = 1
  for i in range(1,N-1):
    ans += A[i]
    cnt += 1
    if cnt==N-1:
      break
    ans += A[i]
    cnt += 1
    if cnt==N-1:
      break
  return ans
print(solve())