def solve():
  N, K = map(int, input().split())
  H = list(map(int, input().split()))
  if K>=N:
    return 0
  H.sort()
  ans = sum(H[:N-K])
  return ans
print(solve())