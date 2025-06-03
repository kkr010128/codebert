from decimal import Decimal
a,b,c=map(Decimal,input().split())
print('Yes' if a.sqrt()+b.sqrt()<c.sqrt() else 'No')