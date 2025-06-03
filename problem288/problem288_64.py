def solve(n):
  l = []
  for i in range(int(n**(1/2))):
    if n % (i+1) == 0:
      a = i + 1
      b = n // a
      l.append(a+b-2)
  return min(l)

print(solve(int(input())))