'''
Created on 2020/08/20

@author: harurun
'''
def main():
  import itertools
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N=int(pin())
  S=[]
  T=[]
  for _ in [0]*N:
    s,t=pin().split()
    S.append(s)
    T.append(int(t))
  U=list(itertools.accumulate(T))
  X=pin()[:-1]
  print(sum(T)-U[S.index(X)])
  return 

main()