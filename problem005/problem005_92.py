import sys
  
for m,n in [map(int,x.split()) for x in list(sys.stdin)]:
    g,r = m,n
    while r!=0:
      g,r = r,g%r
    print(g,m//g*n)