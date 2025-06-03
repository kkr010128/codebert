N = int(input())

import sys
if N & 1:
    print(0)
    sys.exit()

ans = 0
N //= 2
while N != 0:
    ans += N // 5
    N //= 5

print(ans)