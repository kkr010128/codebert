N = int(input())

ans=[0]*N

for x in range(1,101):
  for y in range(1,101):
    for z in range(1,101):
      F=x**2 + y**2 + z**2 + x*y + y*z + z*x
      if(N>=F):
        ans[F-1] += 1
        
for i in ans:
  print(i)