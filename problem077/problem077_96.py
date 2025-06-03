'''
Created on 2020/09/14

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  a,b,c,d=map(int,pin().split())
  print(max(a*c,a*d,b*c,b*d))
  return
main()