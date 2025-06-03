import math
n=int(input())
z=100000
for i in range(1,n+1):
  z+=z*5/100
  z=(math.ceil(z/1000))*1000
print(z)
