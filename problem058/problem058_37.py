import sys

for i in sys.stdin:
    n,x = map(int,i.split())
    s = 0
    if n==0 and x==0:
      break
    if x <= 3*n-3 and x >= 6:
      for i in range(1,min(n-1,x//3)):
        s += len(range(max(i+1,x-i-n),min(n,(x-i+1)//2)))
    print(s)