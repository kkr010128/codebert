A,B = input().split()

import decimal as d
d.getcontext().rounding = d.ROUND_DOWN
ans = round(d.Decimal(A)*d.Decimal(B),0)
print(ans)
