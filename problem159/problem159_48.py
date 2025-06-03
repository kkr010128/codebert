import math
x = int(input())
a = 100
year = 0

while a < x:
    a = (a * 101)//100
    year += 1
print(year)