def solve(n,m):
  if not n:return 1
  n%=m
  return-~solve(n,bin(n).count('1'))
n=int(input())
s=input()
a=int(s,2)
*x,=map(int,s)
h=sum(x)
try:a,b=a%(h-1),a%(h+1)
except:b=a%(h+1)
for i in range(n):
  if x[i]:
    if not h-1:
      print(0)
      continue
    x[i]=0
    t=(a-pow(2,~i+n,h-1))%(h-1)
  else:
    x[i]=1
    t=(b+pow(2,~i+n,h+1))%(h+1)
  r=solve(t,bin(t).count('1'))
  x[i]^=1
  print(r)