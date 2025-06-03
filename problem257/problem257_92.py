def solve():
  N = int(input())
  A = list(map(int, input().split()))
  ans = 0
  p = 1
  for a in A:
    if a==p:
      p += 1
    else:
      ans += 1
  if p==1:
    ans = -1
  return ans
print(solve())