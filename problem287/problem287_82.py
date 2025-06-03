n = int(input())
a = 0
for i in range(1,10):
  for j in range(1,10):
    if(n==i*j):
      a+=1
if(a>=1):
  print("Yes")
else:
  print("No")