def solve():
  A, B, C, K = map(int, input().split())
  ans = min(A,K)-max(0,K-A-B)
  return ans
print(solve())