import numpy as np

D = int(input())
c = np.array( list(map(int, input().split())) )
s = [[] for i in range(365+1)]
for i in range(D):
  s[i] = np.array( list(map(int, input().split())) )
#
last = np.array( [-1]*26 )
av = np.array( [0]*26 )
id = np.identity(4,dtype=int)

v = 0
for d in range(D):
  av = s[d] - sum( c*(d-last) ) + c*(d-last) 
  t =  int(input())
  t -= 1
  last[t] = d
  v += av[t]
  print( v )
#
