n, a, b = map(int, input().split())
red = 0 ; blue = 0
if n >= a + b :
    stack = n // (a+b)
    red += b * stack
    blue += a * stack
    n -= (a+b) * stack
if n > a :
    n -= a
    blue += a
else :
    blue += n
if n > b :
    n -= b
    red += b
else :
    red += n
print(blue)
