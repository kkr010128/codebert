import math
while True:
  n=int(input())
  if n==0:
    break
  s=[int(0) for i in range(n)]
  s[:]=(int(x) for x in input().split())
  
  m=sum(s)/n
  a2=0
  for i in range(n):
    a2+=(s[i]-m)**2
  a2/=n
  print('{:.05f}'.format(math.sqrt(a2)))


