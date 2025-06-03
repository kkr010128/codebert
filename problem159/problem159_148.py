X = int(input())
a = 100
year = 0
import math
while True:
    a = a*101//100
    year += 1
    if a >= X:
        break
print(year)