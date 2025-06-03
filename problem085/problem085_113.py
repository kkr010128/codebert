from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))
from math import gcd

n=int(input())
a=lnii()

g=a[0]
for i in range(n):
  g=gcd(g,a[i])

def factorization(n):
    p=2
    fcr=set()
    while p*p<=n:
        while n%p==0:
            fcr.add(p)
            n//=p
        p+=1
    if n>1:
        fcr.add(n)
    return fcr

def eratosthenes(lim):
  is_p=[1]*lim

  is_p[0]=0
  is_p[1]=0

  for i in a:
    fcr=factorization(i)
    for j in fcr:
      if is_p[j]:
        for k in range(j,lim,j):
          is_p[k]=0
      else:
        if g==1:
          print('setwise coprime')
        else:
          print('not coprime')
        exit()
  return is_p

lim=10**6+1
is_p=eratosthenes(lim)

print('pairwise coprime')