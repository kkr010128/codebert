import decimal
a,b=map(str,input().split())
RES = decimal.Decimal(a)*decimal.Decimal(b)
res = int(RES)
print(res)