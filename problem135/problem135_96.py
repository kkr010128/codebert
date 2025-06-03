#decimalを使った別解
import decimal
deci = decimal.Decimal
a,b = input().split()
x,y = deci(a),deci(b)
ans = (x*y).quantize(deci('0'),rounding=decimal.ROUND_FLOOR)
print(ans)