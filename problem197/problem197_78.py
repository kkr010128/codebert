line = input()
 
data = line.split()
 
import math
a =int(data[0])
b =int(data[1])
c =int(data[2])
if c-a-b>0:
  if(-a-b+c)*(-a-b+c) >a*b*4:
    print("Yes")
  else:
    print("No")
else:
  print("No")

