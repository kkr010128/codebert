n=int(input())

a=[0]*n

for x in range(1,101):
  for y in range(1,101):
    for z in range(1,101):
      k=x*x+y*y+z*z+x*y+y*z+z*x
      if k <=n:
        a[k-1]+=1
        
for q in range(n):
  print(a[q])