import math

n = int(input())
debt = 100000
for _ in range(n):
    debt = debt * 1.05
    debt = math.ceil(debt / 1000) * 1000
print(debt)

