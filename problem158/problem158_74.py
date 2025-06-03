a=input()
a=int(a)
b=input()
b=b.split()

import numpy as np

c=np.arange(int(b[0]),int(b[1])+1)
z=0
for x in c:
  if x%a==0:
    z=z+1

if z==0:
  print("NG")
else:
  print("OK")
