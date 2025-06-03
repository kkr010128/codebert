import math
n = int(input())

def f(x,y,z):
  return x**2 + y**2 + z**2 + z*x + x*y + y*z

current = [1,1,1]
ans = 0
p = [0 for _ in range(n+1)]
m = math.ceil(math.sqrt(n))+1
for i in range(1, m):
  f_ = f(i, 1, 1)
  if f_ > n:
    break
  for j in range(1, m):
    f_ = f(i,j,1)
    if f_ > n:
      break
    for k in range(1, m):
      f_ = f(i,j,k)
      if f_ > n:
        break
      p[f_] += 1
for i in range(1, n+1):
  print(p[i])