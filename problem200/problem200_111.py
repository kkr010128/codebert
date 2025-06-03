'''
Created on 2020/08/20

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  
  A,B,M=map(int,pin().split())
  a=list(map(int,pin().split()))
  b=list(map(int,pin().split()))
  
  ans=min(a)+min(b)
  
  for _ in [0]*M:
    x,y,c=map(int,pin().split())
    t=a[x-1]+b[y-1]-c 
    if t<ans:
      ans=t 
  print(ans)
  return 

main()