#57
import decimal
a,b = map(int,input().split())

for i in range(1,10001):
    num1 = int(i*decimal.Decimal("0.08"))
    num2 = int(i*decimal.Decimal("0.1"))
    if num1 == a and num2 == b:
        print(i)
        break
    if int(i*decimal.Decimal("0.08")) > a:
        print("-1")
        break