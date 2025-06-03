def solve(a,b,k):
  if k <= a: return a - k, b
  elif k <= a + b: return 0, b - (k - a)
  else: return 0, 0

a,b,k = map(int,input().split())
ans_1, ans_2 = solve(a,b,k)
print(f"{ans_1} {ans_2}")