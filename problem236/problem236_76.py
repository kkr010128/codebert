'''
Created on 2020/08/20

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  H=int(pin())
  W=int(pin())
  N=int(pin())
  t=max(H,W)
  if N%t==0:
    print(N//t)
  else:
    print(N//t+1)
  return 

main()