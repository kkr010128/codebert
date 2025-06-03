a,b = map(int,input().split())

import math

gc = math.gcd(a,b)
ans = int(a*b/gc)
print(ans)