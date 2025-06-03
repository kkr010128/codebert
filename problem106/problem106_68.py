n=int(input())
a=[0]*(n+1)
for x in range(1,101):
  for y in range(1,101):
    for z in range(1,101):
      if x*x+y*y+z*z+x*y+x*z+y*z<=n:
        a[x*x+y*y+z*z+x*y+x*z+y*z]+=1
for i in range(1,n+1):
  print(a[i])