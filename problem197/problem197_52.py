import math
import sys
from decimal import Decimal
a,b,c = map(int,input().split())
if c-a-b <= 0:
	print('No')
	sys.exit()
if Decimal((c-a-b)*(c-a-b) - 4*a*b) > 0:
	print("Yes")
else:
	print('No')
