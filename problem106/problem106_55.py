n=int(input())
MAX=(10**4)
cntl=[0]*(MAX+1)

for x in range(1,101):
  for y in range(1,101):
    for z in range(1,101):
      if x**2+y**2+z**2+x*y+y*z+x*z>MAX:
        break
      cntl[x**2+y**2+z**2+x*y+y*z+x*z]+=1
for i in range(1,n+1):
  print(cntl[i])