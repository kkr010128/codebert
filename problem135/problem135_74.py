A,B = input().split()
from decimal import Decimal
A = Decimal(A)
B = Decimal(B)
ans = A*B
ans = str(ans)
n = len(ans)
s = ''
for i in range(n):
    if ans[i] == '.':
        break
    s += ans[i]
print(s)