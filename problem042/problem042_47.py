import sys

i=1
for s in sys.stdin:
  n = int(s)
  if n == 0:
    break
  print("Case ",i,": ",n,sep="")
  i += 1