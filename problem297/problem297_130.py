import math

N = int(input())

if N % 2 == 0:
    ans = 0.5
else :
    ans = math.ceil(N / 2) / N

print(ans)