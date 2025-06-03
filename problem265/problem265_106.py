import math
n = int(input())
x, y = math.floor(n / 1.08), math.ceil(n / 1.08)
ans = ":("
if int(x * 1.08) == n:
    ans = x
elif int(y * 1.08) == n:
    ans = y
print(ans)