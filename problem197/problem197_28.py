import decimal
a,b,c = map(decimal.Decimal,input().split())
print("Yes" if 4*a*b < (c-(a+b))**2 and 0 < c-(a+b) else "No")