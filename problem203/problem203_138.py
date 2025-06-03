import math
a,b=map(int,input().split())

for i in range (11000):
  if a <= i*0.08 <a+1:
    if b<= i*0.1 <b+1:
      print(i)
      exit()
print(-1)