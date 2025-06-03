def if_3(t1,ans1,t2,ans2,ans3):print(ans1 if t1 else ans2 if t2 else ans3)
def if_2(t1,ans1,ans2):print(ans1 if t1 else ans2)
def YN(t):print("YES" if t else "NO")
def yn(t):print("yes" if t else "no")
def Yn(t):print("Yes" if t else "No")
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  x=int(pin())
  if_2(x==1,0,1)
  return
main()