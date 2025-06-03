import numpy as np

D = int(input())
c = np.array( list(map(int, input().split())) )
#
s = [[] for i in range(D)]
for i in range(D):
  s[i] = np.array( list(map(int, input().split())) )
#
v = 0
cc =  np.array( [0]*26 )
last = np.array( [-1]*26 )
for d in range(D):
  cc += c
  av = s[d] - sum( cc ) + cc
  av2 = av + cc*min((D-d-1),13)
  m = max(av2)
  for t in range(26):
    if av2[t] == m:
      cc[t] = 0
      v += av[t]
      print(t+1)
      break
#
#print( v )
