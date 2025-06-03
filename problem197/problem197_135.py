from decimal import Decimal
a,b,c=[Decimal(int(i)) for i in input().split()]
l=a.sqrt()+b.sqrt()
r=c.sqrt()
print("Yes" if l < r else "No")
