import math

n, x, t = map(int, input().split())

count = math.ceil(n / x)

time = t * count

print(time)