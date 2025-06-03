N = int(input())

A = [0] * (N+1)

for x in range(1,101):
  for y in range(1,101):
    for z in range(1,101):
      wk = x**2 + y**2 + z**2 + x*y + y*z + z*x
      if wk <= N:
        A[wk] += 1
        
for i in range(1,N+1):
  print(A[i])