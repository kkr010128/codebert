import math
while True:
  n=int(input())
  if n == 0:
    break
  p=list(map(int,input().split()))
  m=sum(p)/n
  h=0
  for i in range(n):
    h+=(p[i]-m)**2
  print(math.sqrt(h/n))
