def solve(x):
  if len(x) <= 1:
    return 0
  else:
    return (1 if x[0] != x[-1] else 0) + solve(x[1:-1])

s = input()
print(solve(s))