import sys
from math import gcd
#import numpy as np
#import math
from fractions import Fraction
import itertools

input=sys.stdin.readline
def main():
  ans=1
  mod=1000000007
  n0=0
  na=nb=0
  n=int(input())
  d={}

  for i in range(n):
      a,b=map(int,input().split())
      if b==0 and a==0:
          n0+=1
      elif b==0:
          nb+=1
      elif a==0:
          na+=1
      else:
          g=gcd(a,b)
          if b<0:
            a*=-1
            b*=-1
          s=(a//g,b//g)
          if s not in d:
              d[s]=1
          else:
              d[s]+=1
  for k,v in d.items():
      a,b=k
      if a>0:
        if (-b,a) in d:
            if d[(a,b)]!=-1:
                ans*=pow(2,d[(-b, a)])-1+pow(2,d[(a,b)])-1+1
                ans=ans%mod
                d[(-b,a)]=-1
        else:
            ans*=pow(2,d[(a,b)])
            ans=ans%mod
            
      else:
        if (b,-a) in d:
            if d[(a,b)]!=-1:
                ans*=pow(2,d[(b, -a)])-1+pow(2,d[(a,b)])-1+1
                ans=ans%mod
                d[(b,-a)]=-1
        else:
            ans*=pow(2,d[(a,b)])
            ans=ans%mod
  ans*=pow(2,na)-1+pow(2,nb)-1+1
  print((ans-1+n0)%mod)

if __name__ == '__main__':
    main()