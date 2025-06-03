N,R=[int(i) for i in input().split()] 

if N < 10:
  R += 100 * (10- N)
  print(R)
else:
  print(R)