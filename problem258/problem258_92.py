#E
import math
n = int(input())
ans = 0
i = 1
if n % 2 == 0:
    tmp = 5 ** i * 2
    while tmp <= n:
        tmp = 5 ** i * 2
        ans += n //tmp
        i += 1
    print(ans)
else:
    print(0)