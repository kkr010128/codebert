import math

n, m = map(int, input().split())
x = 0
y = 0
if n >= 2:
    x = math.factorial(n) // ((math.factorial(n-2))*2)
elif n <= 1:
    x = 0
if m >= 2:
    y = math.factorial(m) // ((math.factorial(m-2))*2)
elif m <= 1:
    y = 0
print(x + y)