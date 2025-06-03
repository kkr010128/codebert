import math

N = int(input())

a = math.ceil(N / 1000)

b = 1000*a - N

print(b)