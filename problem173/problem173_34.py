import math
n = int(input())
x = n * (n + 1) / 2
f = math.floor(n / 3)
fizzsum = f * (f + 1) / 2 * 3
b = math.floor(n / 5)
buzzsum = b * (b + 1) / 2 * 5
fb = math.floor(n / 15)
fizzbuzzsum = fb * (fb + 1) / 2 * 15
print(int(x - fizzsum - buzzsum + fizzbuzzsum))