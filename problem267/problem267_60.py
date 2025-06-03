'''
Created on 2020/09/04

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  N=int(pin())
  S=pin()[:-1]

  cnt=0
  l=["0","1","2","3","4","5","6","7","8","9"]
  for i in l:
    for j in l:
      for k in l:
        c=[i,j,k]
        n=0
        for m in S:
          if m==c[n]:
            if n==2:
              cnt+=1
              break
            else:
              n+=1
  print(cnt)
  return
main()
#解説AC