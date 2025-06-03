from decimal import *
a,b = map(str,input().split())
a,b = Decimal(a),Decimal(b)

ans = a*b
print(int(ans))