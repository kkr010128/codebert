def solve():
  N, K = map(int, input().split())
  H = list(map(int, input().split()))
  H.sort()
  ans = sum(H[:max(N-K,0)])
  return ans
print(solve())