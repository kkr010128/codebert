'''
Created on 2020/08/31

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  N,M=map(int,pin().split())
  ans=[0]*N
  for _ in [0]*M:
    s,c=map(int,pin().split())
    if s==1 and c==0 and N!=1:
      print(-1)
      return 
    if ans[s-1]!=0 and ans[s-1]!=c:
      print(-1)
      return
    ans[s-1]=c
  if N==3:
    if ans[0]==0:
      if ans[1]==0:
        print(f"{1}{0}{ans[2]}")
      else:
        print(f"{1}{ans[1]}{ans[2]}")
      return
    else:
      print(f"{ans[0]}{ans[1]}{ans[2]}")
      return
  elif N==2:
    if ans[0]==0:
      print(f"{1}{ans[1]}")
    else:
      print(f"{ans[0]}{ans[1]}")
    return
  else:
    print(ans[0])
    return
  return
main()