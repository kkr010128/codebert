from math import sqrt
def solve(n):
  s = list(map(float,input().split()))
  m = sum(s)/n
  a = sqrt(sum([(si-m)**2 for si in s])/n)
  print('{0:.6f}'.format(a))

while True:
  n = int(input())
  if n==0:break
  solve(n)
