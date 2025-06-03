from math import sqrt
from math import floor
n = int(input())
ans = 10 ** 12
m = floor(sqrt(n))
for i in range(1,m+1):
    if n % i == 0:
        j = n // i
        ans = min(ans,i+j-2)
print(ans)