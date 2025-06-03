n=int(input())
j=10501
l=[0 for i in range(j)]
for x in range(1,101):
  for y in range(1,101):
    for z in range(1,101):
      v=x*x+y*y+z*z+y*x+x*z+z*y
      if(v<j):
        l[v]+=1
for i in range(n):
  print(l[i+1])