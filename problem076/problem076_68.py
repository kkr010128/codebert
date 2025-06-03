'''
Created on 2020/09/14

@author: harurun
'''
def yn(t):
  if t:print("yes")
  else:print("no")
  return
def YN(t):
  if t:print("YES")
  else:print("NO")
  return
def Yn(t):
  if t:print("Yes")
  else:print("No")
  return
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  x=int(pin())
  if x==1:
    print(0)
  else:
    print(1)
  return 
main()