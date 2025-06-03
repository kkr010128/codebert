'''
Created on 2020/08/31

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  N=int(pin())
  ans=""
  while N:
    N-=1
    ans+=chr(97+N%26)
    N=N//26
  print(ans[::-1])
  return
main()
#解説AC