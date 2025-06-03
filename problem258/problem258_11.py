import math

N = int(input())

if N % 2 == 1:
    print(0)
else:
    i = 10
    ans = 0
    while(True):
        a = math.floor(N // i)
        if a < 1:
            break
        ans += a
        i *= 5
    print(ans)