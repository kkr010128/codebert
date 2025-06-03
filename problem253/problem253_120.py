import math

def solve(n,a,b):
  diff = b - a
  if diff % 2 == 0:
    return (diff + 1) // 2
  
  # foward to "1" table and A stay 1 round
  root_a = a
  # A kicks back to B
  root_a += diff // 2
  # foward to "N" table B stay 1 round
  root_b = n - b + 1
  # B kicks back to A
  root_b += diff // 2
  
  return min(root_a, root_b)

n, a, b = map(int,input().split())
ans = solve(n,a,b)
print(ans)