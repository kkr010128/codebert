import math

N, D = map(int,input().split())

a = []
n = 0
for i in range(N):
  p,q = map(int, input().split())
  z = math.sqrt(p**2+q**2)
  if z <= D:
    n+=1
    
#print (a)
print (n)