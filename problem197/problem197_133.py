from decimal import Decimal, getcontext
a,b,c = input().split()
getcontext().prec = 65
a = Decimal(a).sqrt()
b = Decimal(b).sqrt()
c = Decimal(c).sqrt()
if a+b < c:
	print("Yes")
else:
  	print("No")
