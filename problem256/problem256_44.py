import math

a, b = map(int, input().split())

if a%b == 0:
    ans = a
elif b%a == 0:
    ans = b
else:
    ans = int(a*b / math.gcd(a, b))

print(ans)