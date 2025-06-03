n=int(input())
num=[0]*60001

for x in range(1,101):
  for y in range(1,101):
    for z in range(1,101):
      i=x*x+y*y+z*z+x*y+y*z+z*x
      if i <= n:
        num[i]+=1
        
for i in range(n):
  print(num[i+1])