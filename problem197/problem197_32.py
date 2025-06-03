from decimal import *
import math
getcontext().prec=1000
a,b,c=map(int,input().split())
if a+b+2*Decimal(a*b).sqrt()<c:
  print("Yes")
else:
  print("No")
